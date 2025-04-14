class News:

    def __init__(self, tit, des, img):

        self.tit = tit
        self.des = des
        self.img = img 

news1 = News(
    "iPhone 16 Pro Max",
    "The iPhone 16 Pro Max will feature a larger 6.9-inch display, powered by the A18 Pro chip with enhanced AI capabilities, and will include a new dedicated Capture button for improved camera functionality.",
    "https://raw.githubusercontent.com/sevinc995/imagess/refs/heads/main/iphone.webp"
)

news2 = News(
    "AirPods Pro 3",
    "The AirPods Pro 3 are expected to feature new adaptive audio technology, improved noise cancellation, and potentialyy offer new color options, They are still in early development stages.",
    "https://github.com/sevinc995/imagess/blob/main/airpods.jpeg?raw=true"
)

news3 = News(
    "Apple Watch Ultra 3",
    "The Apple Watch Ultra 3 will likely maintain  the same rugged design as its prodecessor but may include new health features like blood pressure monitoring and slepp apnea detection, alongside minor hardware upgrades.",
    "https://github.com/sevinc995/imagess/blob/main/watch.jpeg?raw=true"
)

news_list = [news1, news2, news3]