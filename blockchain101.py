//Learning blockchain from https://hackernoon.com/learn-blockchains-by-building-one-117428612f46

class Blockchain(object):
	def __init__(self):
		self.chain = []
		self.current_transacations = []

		self.new_block(previous_hash=1, proof=100)

	def new_block(self,proof, previous_hash=None):
		block = {
			'index': 			len(self.chain) + 1,
			'timestamp':	time(),
			'transactions':	self.current_transacations,
			'proof':			proof,
			'previous_hash': previous_hash or self.hash(self.chain[-1]),
		}

		self.current_transacations = []
		self.chain.append(block)
		return block
		

	def new_transaction(self, sender, recipient, amount):
		self.current_transacations.append({
				'sender'		: sender,
				'recipient'	: recipient,
				'amount'		:	amount,
			})

		return self.last_block['index'] + 1

	@staticmethod
	def hash(block):
		block_string = json.dumps(block, sort_keys=True).encode()
		print(block_string)
		return hashlib.sha256(block_string).hexdigest()

	@property
	def last_block(self):
		return self.chain[-1]