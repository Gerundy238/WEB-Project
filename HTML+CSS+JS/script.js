document.getElementById('message').addEventListener('mouseover', function () {
    this.style.color = 'red'; // �������� ���� ������ ��� ��������� �� �������
});

document.getElementById('message').addEventListener('mouseout', function () {
    this.style.color = ''; // ���������� ���� ������ ��� ����� ����
});
