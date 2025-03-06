class Position:
  title = None
  def __init__(self, title):
    self.title = title
class Department:
  name = None
  def __init__(self, name):
    self.name = name
class User:
  name = None
  position = None
  department = None
  def __init__(self, name, position, department):
    self.name = name
    self.position = position
    self.department = department
developer_position = Position("Software Engineer")
it_department = Department("IT Department")
mikhail = User("Михаил", developer_position, it_department)
print(f"Name: {mikhail.name}")
print(f"Position: {mikhail.position.title}")
print(f"Department: {mikhail.department.name}")
