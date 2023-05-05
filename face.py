from deepface import DeepFace
import json

img = 'photos/image_handler.jpg'


def face_verify(img1):
    print('face_verify start')
    try:
        # model_name='Facenet512'
        result = DeepFace.verify(img1_path=img1, img2_path=img)
        print(result)

        with open('json/result.json', 'w') as file:
            # json.dump(list(result), file, indent=4, ensure_ascii=False)
            json.dump(str(result), file)
            # json.dump(result, file, indent=4, ensure_ascii=False)

        if result.get('verified'):
            return 'is True'
        return 'is False'

    except Exception as e:
        print(e)
        return "Error face"


def face_analyz():
    print('face_analyz start')
    try:
        result = DeepFace.analyze(img_path=img, actions=[
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
        return "Error face"


def sing_registr(img, password):
    pass
