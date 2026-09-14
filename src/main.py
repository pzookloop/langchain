from model import model

if __name__ == '__main__':

    response = model.invoke("你好，请用一句话简短的介绍一下你自己")

    print(response.content)