import base64
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

DISCOVERY_URL = 'https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'


def get_vision_service():
    credentials = GoogleCredentials.get_application_default()
    return discovery.build('vision', 'v1', credentials=credentials,
                           discoveryServiceUrl=DISCOVERY_URL)


def _detect_face(face_file, max_results=4):
    """Uses the Vision API to detect faces in the given file.
    Args:
        face_file: A file-like object containing an image with faces.
    Returns:
        An array of dicts with information about the faces in the picture.
    """
    image_content = face_file.read()
    batch_request = [{
        'image': {
            'content': base64.b64encode(image_content)
        },
        'features': [{
            'type': 'FACE_DETECTION',
            'maxResults': max_results,
        }]
    }]

    service = get_vision_service()
    request = service.images().annotate(body={
        'requests': batch_request,
    })
    response = request.execute()
    if 'faceAnnotations' not in response['responses'][0]:
        return []

    return response['responses'][0]['faceAnnotations']


# [END detect_face]


# [START main]
def detect(input_filename):
    with open(input_filename, 'rb') as image:
        translator = {'LIKELY': 2, 'UNLIKELY': 1, 'VERY_UNLIKELY': 0, 'VERY_LIKELY': 3, 'POSSIBLE': 2}
        faces = _detect_face(image)
        for face in faces:
            joy_likelihood_ = translator[face['joyLikelihood']]
            sorrow_likelihood_ = translator[face['sorrowLikelihood']]
            anger_likelihood = translator[face['angerLikelihood']]
            surprise_likelihood_ = translator[face['surpriseLikelihood']]
            probability = anger_likelihood * -3 + sorrow_likelihood_ * -2 + surprise_likelihood_ * 1 + joy_likelihood_ * 3
            return probability
        return 'NOFACE'
