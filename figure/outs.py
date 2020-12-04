from imageio import imread, imsave
import pandas as pd


def outs(histogram, total):
    """
    这是一个outs的具体实现,返回的是一个二值灰度图像的阈值
    算法链接: https://zh.wikipedia.org/wiki/%E5%A4%A7%E6%B4%A5%E7%AE%97%E6%B3%95#%E7%AE%97%E6%B3%95
    :param histogram: 灰度图像不同灰度级的256元直方图
    :param total: 给定图像的像素数
    :return: 一个二值灰度图像的阈值

    """
    # 总的像素数
    su = 0
    for i in range(1, 256):
        su += i * histogram[i - 1]
    sumB = 0
    wB = 0
    ma = 0
    threshold1 = 0
    threshold2 = 0
    print(len(histogram))
    for i in range(255):
        wB += histogram[i]
        if wB == 0:
            continue
        wF = total - wB

        if wF == 0:
            break

        sumB += i * histogram[i]
        mB = sumB / wB
        mF = (su - sumB) / wF
        between = wB * wF * (mB - mF) * (mB - mF)
        if between >= ma:
            threshold1 = i
            if between > ma:
                threshold2 = i
            ma = between
    return (threshold1 + threshold2) / 2


if __name__ == '__main__':
    im = imread("../test.jpg",  as_gray=True).astype(int)

    ls = []
    for i in range(1, 256):
        a = i
        for j in im:

            for k in j:

                if k == i:
                    a += 1
        ls.append(a)
    threshold = outs(ls, len(im) * len(im[0]))
    print(threshold)
    im[im > threshold] = 0
    imsave("./f.jpg", im, as_gray=True)
