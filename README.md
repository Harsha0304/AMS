---

```markdown
# 🖥️ IT Asset Management System (AMS)

This is a Django-based IT Asset Management System designed to help IT departments efficiently manage hardware and software assets. The system includes functionality for tracking laptops, desktops, servers, virtual machines, keyboards, mice, phones, cameras, routers, switches, firewalls, SIMs/dongles, and vendors.

## 🚀 Features

- Add/update/delete/view various asset types.
- Assign assets to employees.
- Track virtual machine info on servers.
- Store IP, OS, credentials for systems.
- Track SIM/Dongle details with extra metadata.
- Manage vendors and purchase details.
- Bulk import and export of assets.
- Secure login and admin dashboard.
- Responsive UI with Django Admin.

## 🧱 Technologies Used

- 🐍 Python 3
- 🌐 Django
- 🗃️ SQLite (default) or PostgreSQL
- 🛠 HTML/CSS (Admin UI)
- 📦 Django Import/Export for bulk data handling

## 📁 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Harsha0304/AMS.git
   cd asset-management-system
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the system:**
   - Open [http://localhost:8000/admin](http://localhost:8000/admin)

## 📦 Bulk Import/Export

- Available directly from Django Admin.
- Supports importing/exporting CSV/Excel for all major models.

## 📊 Asset Types Supported

- Laptops, Desktops, Servers, VMs
- Network Switches, Firewalls, Routers
- SIMs/Dongles (with sim_name, phone number, CCID, etc.)
- Phones, Cameras
- Keyboards, Mice
- Vendor tracking
- Employee assignments

## 👨‍🔧 Contributor

**Harsha**  
🔧 DevOps Engineer @ ABI Health Technologies  
🌐 [Portfolio](https://harsha0304.github.io/portfolio/)
