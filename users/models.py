from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('employee', 'Employee'),
        ('company_owner', 'Company Owner'),
        ('legal_team', 'Legal Team'),
        ('investigator', 'Investigator'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)  # For soft delete

    def __str__(self):
        return f"{self.username} ({self.role})"
    
    
    
# 💡 Why did you use this CustomUser?
# Because in your project (ZeroLeak), different users do different jobs:

# Role	        What They Do
# employee	    Bound by NDA, could leak stuff (😈 maybe)
# company_owner	Can upload NDAs, track cases
# legal_team	Confirms if something is really a breach, closes legal cases
# investigator	Investigates reports, flags suspicious employees

# Role	Permissions
# 🧑‍💼 CompanyOwner	Upload NDAs, add employees
# 👨‍⚖️ LegalTeam	View reports, resolve cases
# 🕵️ Investigator	Flag employees, link leaks
# 👨‍💻 Employee	View assigned NDAs

# ✅ NDA App
class NDA(models.Model):
    title = models.CharField(...) #Name of NDA, like "ZeroLeak Agreement Jan 2025"
    document = models.FileField(...) # Actual PDF file upload
    start_date = models.DateField()  # NDA starts from this date
    end_date = models.DateField()   #NDA ends here
    assigned_employees = models.ManyToManyField(CustomUser, limit_choices_to={'role': 'employee'})  


#  NDA is the agreement. SensitiveAsset is what the agreement is protecting.
# ✅ Assets App
class SensitiveAsset(models.Model):
    name = models.CharField(...) #Asset name like "Product Launch Deck"
    content_hash = models.CharField(...)  # store SHA256 or MD5 hash Digital fingerprint (SHA256/MD5) for file detection
    uploaded_by = models.ForeignKey(CustomUser, ...) #Who uploaded it (maybe company owner or legal team)
    linked_nda = models.ForeignKey(NDA, ...) #Which NDA covers this file
    


# ✅ Reports App
class LeakReport(models.Model):
    source_url = models.URLField() #Where the leaked file was seen (ex: pastebin.com/abc123)
    leaked_content = models.TextField() #Text or file content that got leaked
    suspected_asset = models.ForeignKey(SensitiveAsset, ...) #Which original file is it a copy of?
    reported_by = models.ForeignKey(CustomUser, ...) #	Who reported this?
    status = models.CharField(choices=[...]) #open, under_review, resolved, etc.
    
       
# ✅ Cases App
class CaseFile(models.Model):
    related_report = models.ForeignKey(LeakReport, ...) #This case is based on which LeakReport?
    flagged_employees = models.ManyToManyField(CustomUser, limit_choices_to={'role': 'employee'})#Which employees are possibly involved? (multi-select)
    investigation_notes = models.TextField()  #What the investigator found
    verdict = models.CharField(choices=[...]) #final result — guilty, not_guilty, inconclusive
    pdf_export = models.FileField(blank=True, null=True) #final PDF of the case report uploaded here for legal documentation


class NDAAcceptance(models.Model):
    nda = models.ForeignKey(NDA, on_delete=models.CASCADE)
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    accepted_at = models.DateTimeField(auto_now_add=True)
