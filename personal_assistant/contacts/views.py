from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Contact
from .forms import ContactForm
from datetime import date, timedelta
import logging

logger = logging.getLogger(__name__)



@login_required
def contact_list(request):
    days = request.GET.get('days')
    search_query = request.GET.get('search', '')

    if days and days.isdigit():
        days = int(days)
    else:
        days = None

    today = timezone.now().date()
    logger.info(f"Filtering contacts for the next {days} days from {today}")

    contacts = Contact.objects.filter(owner=request.user)

    if search_query:
        contacts = contacts.filter(name__icontains=search_query)

    if days:
        
        filtered_contacts = []
        for contact in contacts:
            if contact.date:
                contact_month_day = (contact.date.month, contact.date.day)
                today_month_day = (today.month, today.day)
                end_month_day = ((today + timedelta(days=days)).month, (today + timedelta(days=days)).day)

                if today_month_day <= contact_month_day <= end_month_day or \
                   (today_month_day <= contact_month_day and end_month_day < today_month_day) or \
                   (end_month_day < today_month_day and contact_month_day <= end_month_day):
                    filtered_contacts.append(contact)
        contacts = filtered_contacts
        logger.info(f"Found {len(filtered_contacts)} contacts")
    else:
        contacts = contacts.order_by('name')

    return render(request, 'contacts/contact_list.html', {'contacts': contacts})
def contact_detail(request, pk):

    contact = get_object_or_404(Contact, pk=pk, owner=request.user)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})

@login_required
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect('contacts:contact_detail', pk=contact.pk) 

    else:
        form = ContactForm()
    return render(request, 'contacts/contact_form.html', {'form': form})

@login_required
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk, owner=request.user)
    
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contacts:contact_detail', pk=contact.pk)
        else:
            print(form.errors)  # Виводить помилки форми, якщо вони є
    else:
        form = ContactForm(instance=contact)

    return render(request, 'contacts/contact_form.html', {'form': form})

@login_required
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk, owner=request.user)
    if request.method == 'POST':
        contact.delete()
        return redirect('contacts:contact_list')
    return render(request, 'contacts/contact_confirm_delete.html', {'contact': contact})

@login_required
def upcoming_birthdays(request, days=7):
    today = date.today()
    
    future_date = today + timedelta(days=days)
    contacts = Contact.objects.filter(
        date__gte=today,
        date__lte=future_date,
        owner=request.user 
    ).order_by('date')

    return render(request, 'contacts/upcoming_birthdays.html', {'contacts': contacts, 'days': days})
