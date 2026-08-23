'''class Dog:
    def __init__(self, name, breed = "None"):
        self.name = name
        self.breed = breed

class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color


jerry = Dog(name = "Jerry")
jerry.breed'''


from xml.parsers.expat import errors


class APIConfig: 
    def __init__(self, api_key, model = "gpt-3.5-turbo", max_tokens = 100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1/chat"

#for development configuration
dev_config = APIConfig("sk-dev-key")

#for production config
prod_config = APIConfig("sk-prod-key", model = "gpt-4", max_tokens= 200)

#accessing the configs
print(dev_config.api_key)  # Output: sk-dev-key
print(prod_config.model)   # Output: gpt-4
print(dev_config.model) #gpt-3.5-turbo
print(dev_config.max_tokens) #100

class DataValidator:
    def __init__(self, errors=None):
        self.errors = errors if errors is not None else []
    
    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"Invalid email: {email}")
            return False
        return True
    
    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"Invalid age: {age}")
            return False
        return True
    
    def get_errors(self):
        return self.errors

# Use the validator
validator = DataValidator()

# Notice: we don't pass self, just the email
validator.validate_email(email="bad-email")
validator.validate_age(age=200)

# Or using positional arguments
validator.validate_email("another-bad-email")
validator.validate_age(150)

print(validator.get_errors())
# ['Invalid email: bad-email', 'Invalid age: 200', 'Invalid email: another-bad-email']


#practical application of classes
class BaseModel:
    def __init__(self, model_name):
        self.model_name = model_name
        self.is_loaded = False
    
    def load(self):
        print(f"Loading {self.model_name}...")
        self.is_loaded = True

class TextModel(BaseModel):
    def __init__(self, model_name, max_length=1000):
        super().__init__(model_name)
        self.max_length = max_length
    
    def process_text(self, text):
        if not self.is_loaded:
            self.load()
        # Truncate if needed
        if len(text) > self.max_length:
            text = text[:self.max_length]
        return f"Processed: {text}"

# Use the model - with named arguments
model = TextModel(model_name="gpt-3.5-turbo", max_length=100)

# Call method - notice no 'self' parameter needed
result = model.process_text(text="Hello world")
print(result)  # Loading gpt-3.5-turbo...
               # Processed: Hello world