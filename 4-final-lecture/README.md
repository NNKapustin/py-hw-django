# Разбор вопросов
1. Настройка возможности загрузки изображений в models - ImageField, FileField, upload_to
2. Настройка settings для работы с файлами MEDIA_URL = "/media/" MEDIA_ROOT = BASE_DIR / "media" STATIC_URL = "/static/" STATIC_ROOT = BASE_DIR / "static"
3. pip install pillow - используется в django для работы с изображениями
4. permissions IsAuthenticatedOrReadOnly
5. Аутентификация по токену
6. После добавления "rest_framework", "rest_framework.authtoken", в INSTALLED_APPS делаем миграции
7. Готового решения IsCreator нет, т.к. не понятно с чем сравнивать, поэтому пишем всегда сами наследуясь от BasePermission в котором есть два метода has_permission - права для всех объектов и has_object_permission - права для определенного объекта
8. Чтобы осталась проверка на редактирование своих объектов и чтение объекта любым пользователем в has_object_permission делаем return request.method in SAFE_METHODS or request.user == obj.author
9. При отправке данных для POST запроса нужно указать Content-Type: application/json
10. При добавлении изображения в запросе нужно указать Content-Type: multipart/form-data
11. Лучше использовать специальные инструменты - Postman, Insomnia. Тип аутентификации выбираем Bearer Token Prefix - Token, Body - Multipart, там выбираем тип поля File и название поля. После загрузки изображения, открыть ее не получится, этим занимаются приложения nginx, apache. Для проверки при разработке нужно прописать в основном urls.py проекта 
    <code><br>from django.conf import settings
    from django.conf.urls.static import static
    if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)</code>
12. Для добавления новых действий, не входящих в CRUD, используется декоратор @action из import rest_framework.decorators. В параметрах указываем methods - при каких типах запроса будет срабатывать, detail - будет ли запрос относиться к обределенному объекту или ко всему списку (т.е. для маршрута '.../posts/1/func_name' при True или '.../posts/func_name' при False). url_path - то что должно быть указано в конце url запроса (нижние подчеркивания в url испольщовать не принято), permission_classes - можно указать определенные разрешения для этого действия иначе будут браться по умолчанию, serializer_classes - указать свой сериалайзер
    <code><br>
    @action(methods=['post'], detail=True, url_path='add-to-favorite',
            permission_classes=[IsAuthenticated],
            serializer_class=PostSerializer)
    def add_to_favorite(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.favorite_by.add(request.user)
        return Response({'status': 'OK'})</code>
13. Для вывода избранного добавляем в сериалайзер поле is_favorite = serializers.SerializerMethodField('is_favorite_check') и добавляем функцию проверки
    <code><br>
    def is_favorite_check(self, obj):
        return obj.favorite_by.filter(id=self.context['request'].user.id).exists()</code><br>
    Если в serializers.SerializerMethodField() не указать функцию будет искать фукцию get_ + имя параметра
    Не забываем добавить поле в список fields
14. Удаление из избранного делается подобно добавлению, только меняем obj.favorite_by.remove(request.user)
    <code><br>
    @action(methods=['post'], detail=True, url_path='remove-from-favorite',
            permission_classes=[IsAuthenticated],
            serializer_class=PostSerializer)
    def remove_from_favorite(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.favorite_by.remove(request.user)
        return Response({'status': 'OK'})</code>
15. Поэтому обычно не делают отдельными действиями добавление и удаление, а реализуют переключение
    <code><br>
    @action(methods=['post'], detail=True, url_path='toggle-favorite',
            permission_classes=[IsAuthenticated],
            serializer_class=PostSerializer)
    def toggle_favorite(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.favorite_by.filter(id=request.user.id).exists():
            obj.favorite_by.remove(request.user)
        else:
            obj.favorite_by.add(request.user)
        return Response(self.get_serializer(instance=obj).data)</code><br>
    У каждого подхода есть свои плюсы и минусы, можно оставить оба подхода
