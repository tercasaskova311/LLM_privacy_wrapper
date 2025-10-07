from privacy_wrapper import LLMPrivacyWrapper

wrapper = LLMPrivacyWrapper({"Alice": "NAME1"})
print(wrapper.encode("Hello Alice"))
