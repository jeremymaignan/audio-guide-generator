import html_parser
import network
import utils
from audio import Audio



def main():
    pages = utils.open_json("wikipedia_pages.json")

    for city, places in pages.items():
        # Create folder
        utils.create_folder(city)
        print("{} {} places found".format(city, len(places.keys())))

        for place, url in places.items():
            # Download wikipedia page
            response = network.download_page(url)
            if not response:
                return

            # Parse html
            content = html_parser.get_page_content(response.content)
            content = html_parser.format_content(content)
            print("{}: {} chapters".format(place, len(content.keys())))

            # Create one audio file per chapter
            for i, (chapter, text) in enumerate(content.items()):
                filename = "{} - {} - {}.mp3".format(place, i+1, chapter)
                print("Creating file: {}/{}".format(city, filename))

                # Due to a bug with the pyttsx3 library, it is necessary to create a new client au each audio file
                audio = Audio()
                audio.save_audio_file(text, "{}/{}".format(city, filename))
                del(audio)

if __name__ == "__main__":
    main()
