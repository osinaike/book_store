from django.contrib import admin


class BookStoreAdminSite(admin.AdminSite):
    site_header = "Book Store Site"
    site_title = "Book Store"
    index_title = "Book Store Admin Interface"
    logout_template = "my_logged_out.html"