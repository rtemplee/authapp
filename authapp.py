from dash import Dash, html

app = Dash(__name__, update_title=None, suppress_callback_exceptions=True)

app.layout = html.Div([
    html.Div('hi')
])

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port="8050", debug=True)