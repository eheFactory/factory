from rest_framework import views
from rest_framework.response import Response
from .serializers import vlAveragingBlurSerializer
from factory.utils import (
    decodeBase64,
    encodeBase64
)

from factory.visionlab import filter

class vlAveragingBlurView(views.APIView):
    def post(self, request):
        imageBase64 = request.data["imageBase64"]
        kernelSize = int(request.data["kernelSize"])
        print(imageBase64)
        img = decodeBase64(base64str=imageBase64)
        resImg = filter.Blur.ablur(img, ksize=(kernelSize, kernelSize))
        resultBase64 = encodeBase64(resImg)
        respData = {
            # "originalImage":imageBase64,
            "resultImage": resultBase64.decode()
        }
        resp = vlAveragingBlurSerializer(respData, many=False).data
        return Response(resp)

class vlMedianBlurView(views.APIView):
    def post(self, request):
        imageBase64 = request.data["imageBase64"]
        kernelSize = int(request.data["kernelSize"])
        print(imageBase64)
        img = decodeBase64(base64str=imageBase64)
        resImg = filter.Blur.mblur(img, ksize=kernelSize)
        resultBase64 = encodeBase64(resImg)
        respData = {
            # "originalImage":imageBase64,
            "resultImage": resultBase64.decode()
        }
        resp = vlAveragingBlurSerializer(respData, many=False).data
        return Response(resp)

class vlGaussianBlurView(views.APIView):
    def post(self, request):
        imageBase64 = request.data["imageBase64"]
        kernelSize = int(request.data["kernelSize"])
        print(imageBase64)
        img = decodeBase64(base64str=imageBase64)
        resImg = filter.Blur.gblur(img, ksize=(kernelSize, kernelSize))
        resultBase64 = encodeBase64(resImg)
        respData = {
            # "originalImage":imageBase64,
            "resultImage": resultBase64.decode()
        }
        resp = vlAveragingBlurSerializer(respData, many=False).data
        return Response(resp)