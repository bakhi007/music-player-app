import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

def play_music(folder, mp3_files, start_index):
    file_path = os.path.join(folder, mp3_files[start_index])

    if not os.path.exists(file_path):
        print("\nFile not found!")
        return

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    current_index = start_index

    print(f"\nNow playing : {mp3_files[current_index]}")
    print("""
Commands:
[P] Pause    [R] Resume
[N] Next     [B] Previous
[S] Stop
[H] Shuffle  [L] Loop
""")

    while True:
        command = input("> ").upper().strip()

        if command == 'P':
            pygame.mixer.music.pause()
            print("Paused")

        elif command == 'R':
            pygame.mixer.music.unpause()
            print("Resumed")

        elif command == 'N':
            current_index = (current_index + 1) % len(mp3_files)
            pygame.mixer.music.load(os.path.join(folder, mp3_files[current_index]))
            pygame.mixer.music.play()
            print(f"Now playing : {mp3_files[current_index]}")

        elif command == 'B':
            current_index = (current_index - 1) % len(mp3_files)
            pygame.mixer.music.load(os.path.join(folder, mp3_files[current_index]))
            pygame.mixer.music.play()
            print(f"Now playing : {mp3_files[current_index]}")

        elif command == 'S':
            pygame.mixer.music.stop()
            print("Stopped")
            return

        else:
            print("Invalid command")

def main():

    try:
        pygame.mixer.init()

    except pygame.error as e:
        print("Audio initialization failed!", e)
        return

    folder = "music"

    if not os.path.isdir(folder):
        print(f"Folder '{folder}' not found!")
        return

    mp3_files = [file for file in os.listdir(folder) if file.endswith(".mp3")]

    if not mp3_files:
        print("No .mp3 files found!")    

    while True:
        print("""
███╗   ███╗██╗   ██╗███████╗██╗ ██████╗    ██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗ 
████╗ ████║██║   ██║██╔════╝██║██╔════╝    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗
██╔████╔██║██║   ██║███████╗██║██║         ██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝
██║╚██╔╝██║██║   ██║╚════██║██║██║         ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗
██║ ╚═╝ ██║╚██████╔╝███████║██║╚██████╗    ██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝    ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
""")
        print("List:")

        for index, song in enumerate(mp3_files, start=1):
            print(f"{index}. {song}")

        choice_input = input("\nEnter the song number or press 'Q' to quit : ").upper().strip()
        if choice_input == 'Q':
            print("Bye\n")
            break

        if not choice_input.isdigit():
            print("\nEnter a valid number!")
            continue

        choice = int(choice_input) - 1
        if 0 <= choice < len(mp3_files):
            play_music(folder, mp3_files, choice)
        else:
            print("\nInvalid choice")

if __name__ == "__main__":
    main()