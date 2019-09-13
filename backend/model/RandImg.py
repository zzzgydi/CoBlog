# -*- coding: utf-8 -*-
import base64
import io
import random
from context.config import CurConfig
from PIL import Image, ImageDraw, ImageFont, ImageFilter

_letter_cases = "abcdefghjkmnpqrstuvwxy"  # 小写字母，去除可能干扰的i，l，o，z
_upper_cases = _letter_cases.upper()  # 大写字母
_numbers = '0987654321'  # 数字
init_chars = ''.join((_letter_cases, _upper_cases, _numbers))
'''
todo: 生成验证码图片
- size: 图片的大小，格式（宽，高），默认为(120, 30)
- chars: 允许的字符集合，格式字符串
- img_type: 图片保存的格式，可选的为GIF，JPEG，TIFF，PNG
- mode: 图片模式，默认为RGB
- bg_color: 背景颜色，默认为白色
- fg_color: 前景色，验证码字符颜色
- font_size: 验证码字体大小
- font_type: 验证码字体的详细路径
- length: 验证码字符个数
- point_chance: 干扰点出现的概率，大小范围[0, 100]
'''

# 获得验证码
def create_validate_code(
        size=(100, 36),
        chars=init_chars,
        img_type="png",
        mode="RGB",
        bg_color=(230, 230, 230),
        fg_color=(18, 18, 18),
        font_size=22,
        font_type=CurConfig.FONT_TYPE,
        length=4,
        point_chance=3):

    width, height = size  # 宽， 高
    img = Image.new(mode, size, bg_color)  # 创建图形
    draw = ImageDraw.Draw(img)  # 创建画笔

    def create_lines():
        '''绘制干扰线'''
        for i in range(3):  # 干扰线条数
            begin = (random.randint(0, size[0]), random.randint(0, size[1]))
            end = (random.randint(0, size[0]), random.randint(0, size[1]))
            draw.line([begin, end], fill=(20, 10, 12))

    def create_points():
        '''绘制干扰点'''
        chance = min(100, max(0, int(point_chance)))  # 大小限制在[0, 100]
        for w in range(0, width, 2):
            for h in range(height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    draw.point((w, h), fill=fg_color)

    def create_strs():
        '''绘制验证码字符'''
        c_chars = random.sample(chars, length)  # 生成给定长度的字符串，返回列表格式
        strs = '%s ' % ' '.join(c_chars)  # 每个字符前后以空格隔开
        font = ImageFont.truetype(font_type, font_size)
        font_width, font_height = font.getsize(strs)
        draw.text(((width - font_width) / 3, (height - font_height) / 4),
                  strs,
                  font=font,
                  fill=fg_color)
        return ''.join(c_chars)

    create_lines()
    create_points()
    strs = create_strs()

    # 图形扭曲参数
    params = [
        1 - float(random.randint(1, 2)) / 100, 0, 0, 0,
        1 - float(random.randint(1, 10)) / 100,
        float(random.randint(1, 2)) / 500, 0.001,
        float(random.randint(1, 2)) / 500
    ]
    img = img.transform(size, Image.PERSPECTIVE, params)  # 创建扭曲

    buffered = io.BytesIO()
    img.save(buffered, format="JPEG")
    img_str = b"data:image/png;base64," + base64.b64encode(buffered.getvalue())

    # img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 滤镜，边界加强（阈值更大）
    return img_str.decode('utf-8'), strs


if __name__ == '__main__':
    img_str, str = create_validate_code()
    print(img_str)
