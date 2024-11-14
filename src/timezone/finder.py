from transformers import AutoTokenizer, AutoModelForCausalLM

class TimezoneFinder:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-3b-chat-hf")
        self.model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-3b-chat-hf")

    def predict_timezone(self, country, city):
        prompt = f"What is the most likely timezone for {city}, {country}? Respond with only the timezone name. If your not able to determine a timezone do not output"
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=50)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True).strip()