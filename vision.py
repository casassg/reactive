#!/usr/bin/python

# Copyright 2015 Google, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Draws squares around faces in the given image."""

import argparse
import base64
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

# [START get_vision_service]
DISCOVERY_URL = 'https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'


def get_vision_service():
    credentials = GoogleCredentials.get_application_default()
    return discovery.build('vision', 'v1', credentials=credentials,
                           discoveryServiceUrl=DISCOVERY_URL)


# [END get_vision_service]


# [START detect_face]
def detect_face(face_file, max_results=4):
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
    # print(response)

    return response['responses'][0]['faceAnnotations']


# [END detect_face]


# [START main]
def main(input_filename, output_filename):
    with open(input_filename, 'rb') as image:
        translator = {'LIKELY':2,'UNLIKELY':1, 'VERY_UNLIKELY':0,'VERY_LIKELY':3}
        faces = detect_face(image)
        # print faces
        print('Found %s face%s' % (len(faces), '' if len(faces) == 1 else 's'))
        for face in faces:
            print('============')
            joy_likelihood_ = translator[face['joyLikelihood']]
            print("joy:" + str(joy_likelihood_))
            sorrow_likelihood_ = translator[face['sorrowLikelihood']]
            print("sorrow:" + str(sorrow_likelihood_))
            anger_likelihood = translator[face['angerLikelihood']]
            print("anger:" + str(anger_likelihood))
            surprise_likelihood_ = translator[face['surpriseLikelihood']]
            print("surprise:" + str(surprise_likelihood_))
            probability = anger_likelihood*-3+sorrow_likelihood_*-2+surprise_likelihood_*1+joy_likelihood_*3
            print probability
            return probability
        #
        # print('Writing to file %s' % output_filename)
        # Reset the file pointer, so we can read the file again


# [END main]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Detects faces in the given image.')
    parser.add_argument(
        'input_image', help='the image you\'d like to detect faces in.')
    parser.add_argument(
        '--out', dest='output', default='out.jpg',
        help='the name of the output file.')
    args = parser.parse_args()

    main(args.input_image, args.output)
