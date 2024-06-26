# Generated by Django 4.2.10 on 2024-03-03 00:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('email_verification_token', models.CharField(blank=True, max_length=255, null=True)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GuestProfile',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='guest_profiles')),
                ('year_of_birth', models.PositiveIntegerField(choices=[(1920, '1920'), (1921, '1921'), (1922, '1922'), (1923, '1923'), (1924, '1924'), (1925, '1925'), (1926, '1926'), (1927, '1927'), (1928, '1928'), (1929, '1929'), (1930, '1930'), (1931, '1931'), (1932, '1932'), (1933, '1933'), (1934, '1934'), (1935, '1935'), (1936, '1936'), (1937, '1937'), (1938, '1938'), (1939, '1939'), (1940, '1940'), (1941, '1941'), (1942, '1942'), (1943, '1943'), (1944, '1944'), (1945, '1945'), (1946, '1946'), (1947, '1947'), (1948, '1948'), (1949, '1949'), (1950, '1950'), (1951, '1951'), (1952, '1952'), (1953, '1953'), (1954, '1954'), (1955, '1955'), (1956, '1956'), (1957, '1957'), (1958, '1958'), (1959, '1959'), (1960, '1960'), (1961, '1961'), (1962, '1962'), (1963, '1963'), (1964, '1964'), (1965, '1965'), (1966, '1966'), (1967, '1967'), (1968, '1968'), (1969, '1969'), (1970, '1970'), (1971, '1971'), (1972, '1972'), (1973, '1973'), (1974, '1974'), (1975, '1975'), (1976, '1976'), (1977, '1977'), (1978, '1978'), (1979, '1979'), (1980, '1980'), (1981, '1981'), (1982, '1982'), (1983, '1983'), (1984, '1984'), (1985, '1985'), (1986, '1986'), (1987, '1987'), (1988, '1988'), (1989, '1989'), (1990, '1990'), (1991, '1991'), (1992, '1992'), (1993, '1993'), (1994, '1994'), (1995, '1995'), (1996, '1996'), (1997, '1997'), (1998, '1998'), (1999, '1999'), (2000, '2000'), (2001, '2001'), (2002, '2002'), (2003, '2003'), (2004, '2004'), (2005, '2005'), (2006, '2006'), (2007, '2007'), (2008, '2008'), (2009, '2009'), (2010, '2010'), (2011, '2011'), (2012, '2012'), (2013, '2013'), (2014, '2014'), (2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023')])),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('accounts.customuser',),
        ),
        migrations.CreateModel(
            name='HostProfile',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('podcast_name', models.CharField(max_length=255)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='host_profiles')),
                ('year_of_birth', models.PositiveIntegerField(choices=[(1920, '1920'), (1921, '1921'), (1922, '1922'), (1923, '1923'), (1924, '1924'), (1925, '1925'), (1926, '1926'), (1927, '1927'), (1928, '1928'), (1929, '1929'), (1930, '1930'), (1931, '1931'), (1932, '1932'), (1933, '1933'), (1934, '1934'), (1935, '1935'), (1936, '1936'), (1937, '1937'), (1938, '1938'), (1939, '1939'), (1940, '1940'), (1941, '1941'), (1942, '1942'), (1943, '1943'), (1944, '1944'), (1945, '1945'), (1946, '1946'), (1947, '1947'), (1948, '1948'), (1949, '1949'), (1950, '1950'), (1951, '1951'), (1952, '1952'), (1953, '1953'), (1954, '1954'), (1955, '1955'), (1956, '1956'), (1957, '1957'), (1958, '1958'), (1959, '1959'), (1960, '1960'), (1961, '1961'), (1962, '1962'), (1963, '1963'), (1964, '1964'), (1965, '1965'), (1966, '1966'), (1967, '1967'), (1968, '1968'), (1969, '1969'), (1970, '1970'), (1971, '1971'), (1972, '1972'), (1973, '1973'), (1974, '1974'), (1975, '1975'), (1976, '1976'), (1977, '1977'), (1978, '1978'), (1979, '1979'), (1980, '1980'), (1981, '1981'), (1982, '1982'), (1983, '1983'), (1984, '1984'), (1985, '1985'), (1986, '1986'), (1987, '1987'), (1988, '1988'), (1989, '1989'), (1990, '1990'), (1991, '1991'), (1992, '1992'), (1993, '1993'), (1994, '1994'), (1995, '1995'), (1996, '1996'), (1997, '1997'), (1998, '1998'), (1999, '1999'), (2000, '2000'), (2001, '2001'), (2002, '2002'), (2003, '2003'), (2004, '2004'), (2005, '2005'), (2006, '2006'), (2007, '2007'), (2008, '2008'), (2009, '2009'), (2010, '2010'), (2011, '2011'), (2012, '2012'), (2013, '2013'), (2014, '2014'), (2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023')])),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('accounts.customuser',),
        ),
    ]
