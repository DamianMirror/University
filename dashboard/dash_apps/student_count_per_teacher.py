import pandas as pd
from django_plotly_dash import DjangoDash
from dash import dcc
from dash import html
from university.repositories import Repository

app = DjangoDash('StudentCountPerTeacher')

# Fetch data
data = Repository.Teachers.student_count_per_teacher()
df = pd.DataFrame(list(data))

# Очікувані назви стовпців
expected_columns = ['user_id', 'user__name', 'user__surname', 'student_count']

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
        'user_id': 'teacher_id',
        'user__name': 'teacher_name',
        'user__surname': 'teacher_surname'
    }, inplace=True)

    # Create figure
    fig = {
        'data': [
            {
                'x': df['teacher_name'] + ' ' + df['teacher_surname'],
                'y': df['student_count'],
                'type': 'bar',
                'name': 'Student Count',
            }
        ],
        'layout': {
            'title': 'Student Count per Teacher'
        }
    }

    # Layout
    app.layout = html.Div([
        html.H1(
            'Student Count per Teacher',
            style={'textAlign': 'center', 'marginBottom': '20px'}
        ),
        dcc.Graph(
            id='student-count-teacher',
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
