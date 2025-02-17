from django.urls import path
from student import views


urlpatterns=[
    path("register/",views.StudentRegistarationView.as_view(),name="student-register"),
    path("signin/",views.SignInView.as_view(),name="signin"),
    path("index/",views.IndexView.as_view(),name="index"),
    path("courses/<int:pk>/",views.CourseDetailView.as_view(),name="course-detail"),
    path("courses/<int:pk>/add-to-cart/",views.AddToCartView.as_view(),name="add-to-cart"),
    path("cart/summery/",views.CartSummeryView.as_view(),name="cart-summery"),
    path("cart/<int:pk>/remove",views.CartDeleteView.as_view(),name="cart-item-delete"),
    path("checkout/",views.CheckOutView.as_view(),name="checkout"),
    path("mycourses/",views.MycourseView.as_view(),name="mycorses"),
    path("courses/<int:pk>/watch",views.LessonDetailView.as_view(),name="lesson-detail"),
    path("payment/verify/",views.PaymentVerificationView.as_view(),name="payment-verify"),
    path("signout/",views.SignOutView.as_view(),name="signout")


    
]