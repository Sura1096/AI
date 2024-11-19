from api import api


def main():
    token = api.get_api_token()

    while True:
        user_input = input("Введите запрос: ")
        if user_input == "":
          break
        result = api.get_chat_completion(token, user_input)
        print("Ответ: ", result)


if __name__ == '__main__':
    main()
