import plotly.express as px
import plotly
import pandas as pd
#import plotly.figure_factory as ff

# Read Dataframe from Excel file
df = pd.read_excel("task.xlsm")

# Assign Columns to variables
tasks = df['Task']
start = df['Start Date']
finish = df['End Date']
complete = df['Status']

# Create Gantt Chart
fig = px.timeline(df, x_start=start, x_end=finish, y=tasks, color=complete, title='Digital Banking Roadmap')

# Upade/Change Layout
fig.update_yaxes(autorange='reversed')
fig.update_layout(
        title_font_size=42,
        font_size=18,
        title_font_family='Arial'
        )

# Interactive Gantt
#fig = ff.create_gantt(df)

# Save Graph and Export to HTML
plotly.offline.plot(fig, filename='Task_Overview_Gantt.html')
