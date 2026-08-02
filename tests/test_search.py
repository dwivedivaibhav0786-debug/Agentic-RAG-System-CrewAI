from tools.search_tool import search_web


if __name__ == "__main__":


    result = search_web(

        "latest artificial intelligence news"

    )


    for item in result:

        print("----------------")

        print(
            item["title"]
        )

        print(
            item["link"]
        )

        print(
            item["snippet"]
        )