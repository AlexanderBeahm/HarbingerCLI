```

Traceback (most recent call last):
  File "c:\Users\PC\source\repos\HarbingerCLI\chatgpt.py", line 72, in <module>
    menu()
  File "c:\Users\PC\source\repos\HarbingerCLI\chatgpt.py", line 66, in menu
    active_converation = send_chat(command, active_conversation)
  File "c:\Users\PC\source\repos\HarbingerCLI\chatgpt.py", line 25, in send_chat
    response = openai.ChatCompletion.create(
  File "C:\Users\PC\source\repos\openaiplayground\env\lib\site-packages\openai\api_resources\chat_completion.py", line 25, in create
    return super().create(*args, **kwargs)
  File "C:\Users\PC\source\repos\openaiplayground\env\lib\site-packages\openai\api_resources\abstract\engine_api_resource.py", line 153, in create
    response, _, api_key = requestor.request(
  File "C:\Users\PC\source\repos\openaiplayground\env\lib\site-packages\openai\api_requestor.py", line 226, in request
    resp, got_stream = self._interpret_response(result, stream)
  File "C:\Users\PC\source\repos\openaiplayground\env\lib\site-packages\openai\api_requestor.py", line 619, in _interpret_response
    self._interpret_response_line(
  File "C:\Users\PC\source\repos\openaiplayground\env\lib\site-packages\openai\api_requestor.py", line 682, in _interpret_response_line
    raise self.handle_error_response(
openai.error.RateLimitError: That model is currently overloaded with other requests. You can retry your request, or contact us through our help center at help.openai.com if the error persists. (Please include the request ID 873541cfc482ff7fd2f9cbfb2d8b4c71 in your message.)
```

Occurred when sending a message to ChatGPT on gpt-3.5-turbo. Need to check for default, common error messages and handle them via the cli somehow.