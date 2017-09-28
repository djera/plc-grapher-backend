from orders.models import Order
def create_orders(num):
    current = num

    while (current > 0):
        '''
        orderNumber = models.CharField(max_length=255, default='')
        client = models.CharField(max_length=255, default='')
        pieces = models.IntegerField(default=0)
        status = models.CharField(
            max_length=255, choices=ORDER_STATUS, default='ready')
        line = models.IntegerField(default=1)  # default should be our line
        completedAt = models.DateTimeField(null=True, blank=True)
        addedAt = models.DateTimeField(auto_now_add=True)
        erpDate = models.DateTimeField(null=True, blank=True)
        productionStartedAt = models.DateTimeField(null=True, blank=True)
        lamellaWidth = models.FloatField(default=0)  # mm
        lamellaThickness = models.FloatField(default=0)
        lamellaLength = models.IntegerField(default=0)
        incomingLamellaThickness = models.FloatField(default=-1)
        incomingLamellaWidth = models.FloatField(default=-1)
        panelLength = models.IntegerField(default=0)
        panelWidth = models.IntegerField(default=0)
        type = models.CharField(max_length=255, choices=TYPES, default='L')
        priority = models.IntegerField(null=True)
        quality = models.CharField(default='', blank=True, max_length=100)
        layerNumber = models.IntegerField(default=0)
        woodType = models.CharField(max_length=100, blank=True, default='')
        erpImport = models.BooleanField(default=False)
        '''
        order = Order()
        order.client = "Noritec"
        order.pieces = 5
        order.status = "todo"
        order.lamellaLength = "10300"
        order.lamellaThickness = "37"
        order.lamellaWidth = "207"
        order.quality = "0"
        order.woodType = "0"
        order.save()

        print('created order %s' % order.orderNumber)
        current -= 1
