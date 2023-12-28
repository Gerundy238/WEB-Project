document.getElementById('message').addEventListener('mouseover', function () {
    this.style.color = 'red'; // Изменяем цвет текста при наведении на надпись
});

document.getElementById('message').addEventListener('mouseout', function () {
    this.style.color = ''; // Сбрасываем цвет текста при уходе мыши
});
