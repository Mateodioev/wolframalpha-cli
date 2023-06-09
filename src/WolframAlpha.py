from wolframalpha import Client as MathClient


def query_api(app_id: str, question: str):
    client = MathClient(app_id)
    res = client.query(question)
    answer = next(res.results).text

    return answer
