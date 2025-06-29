slides_dict = {}
file = open('slides.txt', 'r', encoding='utf-8')
slides = file.read().split('\n')
for slide in slides:
    slide_info = slide.split(':')
    slides_dict[slide_info[0]] = slide_info[1:]
