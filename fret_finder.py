import guitarpro

STRING_TUNINGS = [40, 45, 50, 55, 59, 64]

def get_positions_for_pitch(pitch):
    positions = []
    for string_index, open_string_pitch in enumerate(STRING_TUNINGS):
        fret = pitch - open_string_pitch
        if 0 <= fret <= 24:
            gp_string = 6 - string_index
            positions.append((gp_string, fret))
    return positions

def remap_tab_economically(input_file, output_file):
    song = guitarpro.parse(input_file)
    changes = 0

    for track in song.tracks:
        if track.isPercussionTrack:
            continue

        print(f"Processing track: {track.name}")

        # 1. Find global highest fret across all notes in this track (This will determine which note will be the anchor)
        highest_original_fret = 0
        for measure in track.measures:
            for voice in measure.voices:
                for beat in voice.beats:
                    for note in beat.notes:
                        if note.value > highest_original_fret:
                            highest_original_fret = note.value

        print(f"Global highest fret in track: {highest_original_fret}")

        # 2. Transpose notes using the highest fret as anchor
        for measure in track.measures:
            for voice in measure.voices:
                for beat in voice.beats:
                    for note in beat.notes:
                        pitch = note.realValue
                        original_string = note.string
                        original_fret = note.value

                        possible_positions = get_positions_for_pitch(pitch)
                        if not possible_positions:
                            continue

                        # Find note positions closest to the anchor
                        best_string, best_fret = min(
                            possible_positions,
                            key=lambda pos: abs(pos[1] - highest_original_fret)
                        )

                        print(f"Note pitch {pitch}, original string {original_string}, fret {original_fret}")
                        print(f"Possible positions: {possible_positions}")
                        print(f"Chosen position based on highest fret {highest_original_fret}: string {best_string}, fret {best_fret}")

                        if best_string != original_string or best_fret != original_fret:
                            print(f"Remapping note pitch {pitch}: {original_string}, {original_fret} → {best_string}, {best_fret}")
                            note.string = best_string
                            note.value = best_fret
                            changes += 1

    if changes > 0:
        guitarpro.write(song, output_file)
        print(f"Done! {changes} notes remapped. Saved to {output_file}")
    else:
        print("No notes needed remapping.")

if __name__ == "__main__":
    input_gp_file = "input.gp5"
    output_gp_file = "output_economical.gp5"
    remap_tab_economically(input_gp_file, output_gp_file)
