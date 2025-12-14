import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
import random
import time


class MusicPlayer:
    def __init__(self, folder="music"):
        self.folder = folder
        self.mp3_files = []
        self.current_index = 0
        self.shuffle = False
        self.loop = True

        pygame.mixer.init()
        self.load_songs()

    def load_songs(self):
        if not os.path.isdir(self.folder):
            raise FileNotFoundError(f"Folder '{self.folder}' not found!")

        self.mp3_files = [
            f for f in os.listdir(self.folder) if f.lower().endswith(".mp3")
        ]

        if not self.mp3_files:
            raise ValueError("No .mp3 files found!")

    def play(self, index=None):
        if index is not None:
            self.current_index = index

        song = self.mp3_files[self.current_index]
        path = os.path.join(self.folder, song)

        pygame.mixer.music.load(path)
        pygame.mixer.music.play()

        title = os.path.splitext(song)[0]
        print(f"\n🎵 Now playing: {title}")

    def pause(self):
        pygame.mixer.music.pause()
        print("Paused")

    def resume(self):
        pygame.mixer.music.unpause()
        print("Resumed")

    def stop(self):
        pygame.mixer.music.stop()
        print("Stopped")

    def next_song(self):
        if self.shuffle:
            self.current_index = random.randint(0, len(self.mp3_files) - 1)
        else:
            self.current_index += 1
            if self.current_index >= len(self.mp3_files):
                if self.loop:
                    self.current_index = 0
                else:
                    self.stop()
                    return
        self.play()

    def previous_song(self):
        self.current_index = (self.current_index - 1) % len(self.mp3_files)
        self.play()

    def toggle_shuffle(self):
        self.shuffle = not self.shuffle
        print(f"Shuffle {'ON' if self.shuffle else 'OFF'}")

    def toggle_loop(self):
        self.loop = not self.loop
        print(f"Loop {'ON' if self.loop else 'OFF'}")

    def auto_next(self):
        if not pygame.mixer.music.get_busy():
            self.next_song()

    def show_playlist(self):
        print("\n🎼 Playlist:")
        for i, song in enumerate(self.mp3_files, start=1):
            print(f"{i}. {os.path.splitext(song)[0]}")


def main():
    try:
        player = MusicPlayer()
    except Exception as e:
        print("Error:", e)
        return

    player.show_playlist()

    choice = input("\nPilih lagu (angka): ").strip()
    if not choice.isdigit():
        print("Invalid choice")
        return

    player.play(int(choice) - 1)

    print("""
Commands:
[P] Pause    [R] Resume
[N] Next     [B] Previous
[S] Stop
[H] Shuffle  [L] Loop
[Q] Quit
""")

    while True:
    # auto next kalau lagu selesai
        if not pygame.mixer.music.get_busy():
            player.auto_next()

        cmd = input("> ").upper().strip()

        if cmd == 'P':
            player.pause()
        elif cmd == 'R':
            player.resume()
        elif cmd == 'N':
            player.next_song()
        elif cmd == 'B':
            player.previous_song()
        elif cmd == 'S':
            player.stop()
        elif cmd == 'H':
            player.toggle_shuffle()
        elif cmd == 'L':
            player.toggle_loop()
        elif cmd == 'Q':
            player.stop()
            print("Bye 👋")
            break
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
