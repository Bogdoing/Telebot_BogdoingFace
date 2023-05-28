from deepface import DeepFace
import json
import os

img_def = 'photos/image_handler.jpg'


def face_verify_2(img1, img2):
    print('face_verify start')
    try:
        print('1')
        # model_name='Facenet512'
        if os.path.exists(img1) and os.path.exists(img2):
            result = DeepFace.verify(img1_path=img1, img2_path=img2)
        else:
            print("img not exist")
        print(result)
        print('2')
        with open('json/result.json', 'w') as file:
            # json.dump(list(result), file, indent=4, ensure_ascii=False)
            json.dump(str(result), file)
            # json.dump(result, file, indent=4, ensure_ascii=False)
        print('3')
        if result.get('verified'):
            return 'is True'
        return 'is False'

    except Exception as e:
        print(e)
        return "Error face - face_verify"


def face_analyz():
    print('face_analyz start')
    try:
        result = DeepFace.analyze(img_path=img_def, actions=[
                                  'age', 'gender', 'race', 'emotion'])
        result_dist = dict(result[0])
        with open('json/result_analyz.json', 'w') as file:
            json.dump(result, file, indent=4, ensure_ascii=False)
            # json.dump(result, file, indent=4, ensure_ascii=False)

        print(result)
        print(f'[+] Age: {result_dist.get("age")}')
        print(f'[+] Gender: {result_dist.get("gender")}')
        print(f'[+] Race domain: {result_dist.get("dominant_race")}')
        print(f'[+] Race all: {result_dist.get("race")}')
        print(f'[+] Dominant emotion: {result_dist.get("race")}')

        return result_dist
    except Exception as e:
        print(e)
        return "Error face - face_analyz"


# def face_analyz_2(img):
#     print('face_analyz start')
#     try:
#         result = DeepFace.analyze(img_path=img, actions=[
#                                   'age', 'gender', 'race', 'emotion'])
#         result_dist = dict(result[0])
#         with open('json/result_analyz.json', 'w') as file:
#             json.dump(result, file, indent=4, ensure_ascii=False)
#             # json.dump(result, file, indent=4, ensure_ascii=False)

#         print(result)
#         print(f'[+] Age: {result_dist.get("age")}')
#         print(f'[+] Gender: {result_dist.get("gender")}')
#         print(f'[+] Race domain: {result_dist.get("dominant_race")}')
#         print(f'[+] Race all: {result_dist.get("race")}')
#         print(f'[+] Dominant emotion: {result_dist.get("race")}')

#         return result_dist
#     except Exception as e:
#         print(e)
#         return "Error face - face_analyz"


# def face_verify(img1):
#     print('face_verify start')
#     try:
#         print('1')
#         # model_name='Facenet512'
#         result = DeepFace.verify(img1_path=img1, img2_path=img_def)
#         print(result)
#         print('2')
#         with open('json/result.json', 'w') as file:
#             # json.dump(list(result), file, indent=4, ensure_ascii=False)
#             json.dump(str(result), file)
#             # json.dump(result, file, indent=4, ensure_ascii=False)
#         print('3')
#         if result.get('verified'):
#             return 'is True'
#         return 'is False'

#     except Exception as e:
#         print(e)
#         return "Error face - face_verify"
