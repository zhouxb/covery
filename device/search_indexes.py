from haystack import indexes
from device.models import Device

class DeviceIndex(indexes.RealTimeSearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    os = indexes.CharField(model_attr='os')
    safe = indexes.CharField(model_attr='safe')

    def get_model(self):
        return Device

    #def index_queryset(self):
        #"""Used when the entire index for model is updated."""
        #return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())

