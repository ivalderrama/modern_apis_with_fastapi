import fastapi
import uvicorn
import json


api = fastapi.FastAPI()


@api.get('/sp400/current_year')
def display_final_current_year():
    with open('csv_json_files/20210302/final_curr_year_list.json') as file:
        final_json1 = file.read()
    fin_dict1 = json.loads(final_json1)[0]

    return fin_dict1


@api.get('/sp400/last_year')
def display_last_year():
    with open('csv_json_files/20210302/final_last_year_list.json') as file:
        final_json2 = file.read()
    fin_dict2 = json.loads(final_json2)[0]

    return fin_dict2


@api.get('/sp400/year_before_last')
def display_year_before_last():
    with open('csv_json_files/20210302/final_y_b_last_list.json') as file:
        final_json3 = file.read()
    fin_dict3 = json.loads(final_json3)[0]

    return fin_dict3


@api.get('/sp400/ticker_current_year')
def display_year_before_last():
    with open('csv_json_files/20210302/ticker_curr_year_list.json') as file:
        ticker_json = file.read()

    return json.loads(ticker_json)[0]


@api.get('/sp400/ticker_last_year')
def display_year_before_last():
    with open('csv_json_files/20210302/ticker_last_year_list.json') as file:
        ticker_json = file.read()

    return json.loads(ticker_json)[0]


@api.get('/sp400/ticker_year_before_last')
def display_year_before_last():
    with open('csv_json_files/20210302/ticker_y_b_last_list.json') as file:
        ticker_json = file.read()

    return json.loads(ticker_json)[0]


@api.get('/sp400/result')
def display_result():
    with open('csv_json_files/20210302/fscorefull_result.json') as file:
        result_json = file.read()

    return json.loads(result_json)


if __name__ == '__main__':
    uvicorn.run(api, port=8000, host='127.0.0.1')
