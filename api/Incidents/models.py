import uuid

class Models:

	def __init__(self,id, createdOn, createdBy, location, status, incident_type, images, videos, comment):
		self.id = id
		self.createdOn = createdOn
		self.createdBy = createdBy
		self.location = location
		self.status = status
		self.incident_type = incident_type
		self.images = images
		self.videos = videos
		self.comment = comment
		