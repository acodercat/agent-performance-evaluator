def handover_to_agent(chat_id, agent_id, priority='medium', message=''):
	"""
	This function initiates the handover process to transfer an ongoing chat session from a bot to a live human agent.    
	Parameters:
	chat_id: Unique identifier of the chat session that needs to be transferred.
	agent_id: Unique identifier of the human agent to whom the chat will be transferred.
	priority: The priority level for the chat handover.
	message: An optional message to the agent about the chat or customer.

	"""
	pass

def GET_PARCEL_STATE(parcelTrackingId, includeHistory=False):
	"""
	Determines the current state of the parcel, such as 'In Transit', 'Delivered', or 'Awaiting Pickup', based on the provided tracking ID.    
	Parameters:
	parcelTrackingId: Unique identifier for the parcel used to track its movement and status.
	includeHistory: Determines if the historical states of the parcel should be included in the response.

	"""
	pass

tools = [handover_to_agent, GET_PARCEL_STATE]
