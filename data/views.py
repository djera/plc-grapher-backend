from rest_framework import viewsets, permissions, views
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import HexDataSerializer
from .models import HexData, VariableConfig, DataModelConfig
import binascii

class RootView(views.APIView):
    """
    Root endpoint - use one of sub endpoints.
    """
    permission_classes = (
        permissions.AllowAny,
    )
    urls_mapping = {
        'data': 'data-list',
    }
    urls_extra_mapping = None

    def get_urls_mapping(self, **kwargs):
        mapping = self.urls_mapping.copy()
        mapping.update(kwargs)
        # if self.urls_extra_mapping:
        #    mapping.update(self.urls_extra_mapping)
        # mapping.update(settings.get('ROOT_VIEW_URLS_MAPPING'))
        return mapping

    def get(self, request, format=None):
        print(request)
        return Response(
            dict([(key, reverse(url_name, request=request, format=format))
                  for key, url_name in self.get_urls_mapping().items()])
        )


class DataViewset(viewsets.ModelViewSet):
    permission_classes = ( permissions.IsAuthenticated, )
    serializer_class = HexDataSerializer
    queryset = HexData.objects.all()
    ordering_fields = ('added_at',)
    ordering = ('-added_at',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CompiledData(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        hex = HexData.objects.filter(user=request.user)
        config = DataModelConfig.objects.filter(user=request.user).first()
        variables = VariableConfig.objects.filter(config=config)

        dataArr = []
        for l in hex:
            data = {}
            s = binascii.unhexlify(l.hex_data)
            b = [ord(x) for x in s]
            b_len = len(b)
            for v in variables:
                if v.type == VariableConfig.TYPES[0][0]:
                    if v.startByte < b_len:
                        print(str(b[v.startByte]) + ' % '  + str(pow(2, v.startBit)))
                        value = b[v.startByte] & pow(2, v.startBit)
                        data[v.name] = value

            data["timestamp"] = l.added_at
            dataArr.append(data)
        return Response(dataArr)
