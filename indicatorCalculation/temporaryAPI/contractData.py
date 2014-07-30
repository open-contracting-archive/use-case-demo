
class ContractData(object):
    """A class represents the data in the JSON standard"""
    def __init__(self):

        self.publisher = None
        self.publishingMeta = None
        self.releases = []


class Identifier(object):
    """docstring for Identifier"""
    def __init__(self, parent=None, name=None,
                 scheme=None, uid=None, uri=None):
        self.parent = parent
        self.name = name
        self.scheme = scheme
        self.uid = uid
        self.uri = uri


class PublishingMeta(object):
    '''doctring for PublishingMeta'''
    def __init__(self, date):
        self.date = date


class Release(object):
    """Class representing a release"""
    def __init__(self, contractData=None, releaseMeta=None, buyer=None,
                 planning=None, formation=None, award=None, contract=None,
                 performance=None, additionalProperties=None):

        self.releaseMeta = releaseMeta
        self.buyer = buyer
        self.planning = planning
        self.formation = formation
        self.award = award
        self.contract = contract
        self.performance = performance
        self.additionalProperties = additionalProperties


class ReleaseMeta(object):
    """docstring for ReleaseMeta"""
    def __init__(self, release=None, ocid=None,
                 releaseTag=None, locale='en_US'):
        self.release = release
        self.ocid = ocid
        self.releaseTag = releaseTag
        self.locale = locale


class Tender(object):
    '''docstring for Tender'''
    def __init__(self, release=None, notice=None, itemsToBeProcured=None,
                 totalValue=None, method=None, methodJustification=None,
                 selectionCriteria=None, selectionDetails=None,
                 submissionMethod=None, submissionDetails=None,
                 tenderPeriod=None, clarificationPeriod=None,
                 clarifications=None, awardPeriod=None, numberOfBidders=None,
                 numberOfBids=None, bidders=None, procuringEntity=None,
                 attachments=None, ):

        self.release = release
        self.notice = notice
        self.itemsToBeProcured = itemsToBeProcured or []
        self.totalValue = totalValue
        self.method = method
        self.methodJustification = methodJustification
        self.selectionCriteria = selectionCriteria
        self.selectionDetails = selectionDetails
        self.submissionMethod = submissionMethod
        self.submissionDetails = submissionDetails
        self.tenderPeriod = tenderPeriod
        self.clarificationPeriod = clarificationPeriod
        self.clarifications = clarifications
        self.awardPeriod = awardPeriod
        self.numberOfBidders = numberOfBidders
        self.numberOfBids = numberOfBids,
        self.bidders = bidders or []
        self.procuringEntity = procuringEntity
        self.attachments = attachments or []


class Notice(object):
    """docstring for Notice"""
    def __init__(self, tender=None, id=None, uri=None, publishedDate=None,
                 isAmendment=False, amendment=None):
        super(Notice, self).__init__()
        self.tender = tender
        self.id = id
        self.uri = uri
        self.publishedDate = publishedDate
        self.isAmendment = isAmendment
        self.amendment = amendment


class AmendmentInformation(object):
    """docstring for AmendmentInformation"""
    def __init__(self, amendmentDate=None, amendedFields=None, justification=None):
        super(AmendmentInformation, self).__init__()
        self.amendmentDate = amendmentDate
        self.amendedFields = amendedFields
        self.justification = justification


class Item(object):
    """A good, service, or work to be contracted."""
    def __init__(self, description=None, classificationScheme=None,
                 otherClassificationScheme=None, classificationID=None,
                 classificationDescription=None, unitOfMeasure=None,
                 quantity=None, valuePerUnit=None):
        super(Item, self).__init__()
        self.description = description
        self.classificationScheme = classificationScheme
        self.otherClassificationScheme = otherClassificationScheme
        self.classificationID = classificationID
        self.classificationDescription = classificationDescription
        self.unitOfMeasure = unitOfMeasure
        self.quantity = quantity
        self.valuePerUnit = valuePerUnit

class Value(object):
    """docstring for Value"""
    def __init__(self, ammount=None, currency=None):
        super(Value, self).__init__()
        self.ammount = ammount
        self.currency = currency



class attachment(object):
    """docstring for attachment"""
    def __init__(self, parent=None, description=None, uri=None, lastModefied=None):
        self.parent = parent
        self.description = description
        self.uri = uri
        self.lastModefied = lastModefied


class Period(object):
    """docstring for Period"""
    def __init__(self, startDate=None, endDate=None):
        super(Period, self).__init__()
        self.startDate = startDate
        self.endDate = endDate


class Organization(object):
    """docstring for Organization"""
    def __init__(self, release=None, id=None, additionalProperties=None):
        #super(Buyer, self).__init__()
        #id
        self.id = id
        self.additionalProperties = additionalProperties


class Buyer(Organization):
    """docstring for Buyer"""
    def __init__(self):
        super(Buyer, self).__init__()


class Supplier(Organization):
    """docstring for Supplier"""
    def __init__(self):
        super(Supplier, self).__init__()
