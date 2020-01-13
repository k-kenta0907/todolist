from django.db import models

from users.models import User


class Item(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """

    # 題名
    title = models.CharField(
        verbose_name='イベント名',
        max_length=20,
        blank=True,
        null=True,
    )

    # 内容
    whatisthis = models.TextField(
        verbose_name='内容',
        blank=True,
        null=True,
    )

    # 場所
    place = models.CharField(
        verbose_name='場所',
        max_length=40,
        blank=True,
        null=True,
    )


    # 日付
    date = models.DateField(
        verbose_name='日付',
        blank=True,
        null=True,
    )

    # 状態
    status_choice = (
        (1, '完了'),
        (2, '進行中'),
        (3, '実行前'),
    )

    status = models.IntegerField(
        verbose_name='状態',
        choices=status_choice,
        blank=True,
        null=True,
    )

 

    # 以下、管理項目

    # 作成者(ユーザー)
    created_by = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return self.title

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'サンプル'
        verbose_name_plural = 'サンプル'
