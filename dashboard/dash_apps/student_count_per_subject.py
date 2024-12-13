import pandas as pd
from django_plotly_dash import DjangoDash
from dash import dcc
from dash import html
from university.repositories import Repository

app = DjangoDash('StudentCountPerSubject')

# Fetch data
data = Repository.Subjects.student_count_per_subject()
df = pd.DataFrame(list(data))

# Очікувані назви стовпців
expected_columns = ['id', 'name', 'student_count']

# Перевіряємо, чи всі очікувані стовпці присутні в DataFrame
missing_columns = [col for col in expected_columns if col not in df.columns]
if missing_columns or df.empty:
    # Якщо немає даних або стовпці відсутні
    app.layout = html.Div(
        children=[
            html.H1(
                'Немає даних для відображення',
                style={'textAlign': 'center', 'color': 'red', 'marginTop': '50px'}
            )
        ],
        style={
            'height': '100vh',  # Контейнер займає всю висоту вікна
            'display': 'flex',
            'flexDirection': 'column',
            'justifyContent': 'center',
            'alignItems': 'center',
            'padding': '10px'
        }
    )
else:
    # Перейменовуємо стовпці
    df.rename(columns={
        'id': 'subject_id',
        'name': 'subject_name'
    }, inplace=True)

    # Create figure
    fig = {
        'data': [
            {
                'labels': df['subject_name'],
                'values': df['student_count'],
                'type': 'pie',
                'name': 'Student Count',
            }
        ],
        'layout': {
            'title': 'Student Count per Subject'
        }
    }

    # Layout
    app.layout = html.Div([
        html.H1(
            'Student Count per Subject',
            style={'textAlign': 'center', 'marginBottom': '20px'}
        ),
        dcc.Graph(
            id='student-count-subject',
            figure=fig,
            style={'height': '85vh', 'width': '100%'}  # Графік займає майже всю висоту блоку
        )
    ],
        style={
            'height': '100vh',  # Контейнер займає всю висоту вікна
            'display': 'flex',
            'flexDirection': 'column',
            'justifyContent': 'space-between',
            'padding': '10px'
        }
    )
