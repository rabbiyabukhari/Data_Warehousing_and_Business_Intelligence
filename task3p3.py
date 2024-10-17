from faker import Faker
import pyodbc
import random
#part3
conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-B0IU82M\\SQLEXPRESS;"  
    "Database=Northwind_Rabbiya;"  
    "Trusted_Connection=yes;"
)

cur = conn.cursor()
fake = Faker()

def populate_regions(n):
    for _ in range(n):
        region_id = random.randint(1, 1000)
        region_desc = fake.city_suffix()
        cur.execute(
            "INSERT INTO Regions (RegionID, RegionDescription) VALUES (?, ?)",
            region_id, region_desc
        )

def populate_employees(n):
    ids = []
    for _ in range(n):
        emp_id = random.randint(1, 10000)
        first_name = fake.first_name()
        last_name = fake.last_name()
        title = fake.job()
        prefix = fake.prefix()
        birth_date = fake.date_of_birth(minimum_age=22, maximum_age=65)
        hire_date = fake.date_this_century()
        address = fake.address().replace("\n", ", ")
        city = fake.city()
        region = fake.state_abbr()
        postal_code = fake.zipcode()
        country = fake.country()
        phone = fake.phone_number()
        ext = str(random.randint(100, 999))
        notes = fake.text(max_nb_chars=200)
        photo_path = fake.image_url()
        cur.execute("""
            INSERT INTO Employees (EmployeeID, LastName, FirstName, Title, TitleOfCourtesy, BirthDate, HireDate, Address, City, Region, PostalCode, Country, HomePhone, Extension, Notes, PhotoPath, ReportsTo)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NULL)
        """, emp_id, last_name, first_name, title, prefix, birth_date, hire_date, address, city, region, postal_code, country, phone, ext, notes, photo_path)

        ids.append(emp_id)
    return ids
def update_reports_to(emp_ids):
    for emp_id in emp_ids:
        reports_to = random.choice([eid for eid in emp_ids if eid != emp_id])
        cur.execute(
            "UPDATE Employees SET ReportsTo = ? WHERE EmployeeID = ?",
            reports_to, emp_id
        )
def populate_territories(n):
    cur.execute("SELECT RegionID FROM Regions")
    region_ids = [row[0] for row in cur.fetchall()]
    for _ in range(n):
        terr_id = fake.unique.zipcode()
        terr_desc = fake.city()
        region_id = random.choice(region_ids)
        cur.execute(
            "INSERT INTO Territories (TerritoryID, TerritoryDescription, RegionID) VALUES (?, ?, ?)",
            terr_id, terr_desc, region_id
        )
def populate_employee_territories(n):
    cur.execute("SELECT EmployeeID FROM Employees")
    emp_ids = [row[0] for row in cur.fetchall()]
    cur.execute("SELECT TerritoryID FROM Territories")
    terr_ids = [row[0] for row in cur.fetchall()]

    inserted_pairs = set()
    for _ in range(n):
        emp_id = random.choice(emp_ids)
        terr_id = random.choice(terr_ids)
        if (emp_id, terr_id) not in inserted_pairs:
            cur.execute(
                "INSERT INTO EmployeeTerritories (EmployeeID, TerritoryID) VALUES (?, ?)",
                emp_id, terr_id
            )
            inserted_pairs.add((emp_id, terr_id))
def main():          
    populate_regions(30)
    populate_territories(30)
    emp_ids = populate_employees(30)
    update_reports_to(emp_ids)
    populate_employee_territories(30)
    conn.commit()
    conn.close()
main()
