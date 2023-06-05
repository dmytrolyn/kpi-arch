from filters import reverse, uppercase

def run_pipe_filter(input_data):
    result = uppercase(input_data)
    result = hyphen(result)

    return result

if __name__ == '__main__':
    input_data = 'Hello'
    result = run_pipe_filter(input_data)
    print(result)