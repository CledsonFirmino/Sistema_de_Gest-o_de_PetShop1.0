# Generated by Django 5.0.4 on 2024-05-15 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pet', '0003_alter_cadastro_venda_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro_cliente',
            name='nome_cliente',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cadastro_pet',
            name='pelagem',
            field=models.CharField(choices=[(1, 'Longa'), (2, 'Curta'), (3, 'Encaracolado'), (4, 'Dupla'), (5, 'Peculiar'), (6, 'Longo Ondulado'), (7, 'Textura dura'), (8, 'Textura lisa')], default='1', max_length=50),
        ),
        migrations.AlterField(
            model_name='cadastro_pet',
            name='porte',
            field=models.CharField(choices=[(1, 'Pequeno 6 a 15kg'), (2, 'Médio 15 a 25kg'), (3, 'Grande 25 a 45kg'), (4, ',Gigantes 45 a 90kg')], default='1', max_length=50),
        ),
        migrations.AlterField(
            model_name='cadastro_pet',
            name='raca',
            field=models.CharField(choices=[(1, 'Border Collie'), (2, 'Buldogue francês'), (3, 'Buldogue inglês'), (4, 'Chihuahua'), (5, 'Dachshund'), (6, 'Fila Brasileiro'), (7, 'Fox Terrier'), (8, 'Golden Retriever'), (9, 'Husky'), (10, 'Labrador'), (11, 'Lhasa Apso'), (12, 'Maltês'), (13, 'Pinscher'), (14, 'Poodle'), (15, 'Pug'), (16, 'Pastor'), (17, 'Rottweiler'), (18, 'Schnauzer'), (19, 'Terrier'), (20, 'Yorkshire'), (21, 'Shih Tzu'), (22, 'Schnauzer'), (23, 'SRD (Sem Raça Definida)')], default='23', max_length=50),
        ),
        migrations.AlterField(
            model_name='cadastro_venda',
            name='banho_tipo',
            field=models.CharField(choices=[(1, 'Simples'), (2, 'Composto'), (3, 'Hidratação')], max_length=50),
        ),
        migrations.AlterField(
            model_name='cadastro_venda',
            name='data',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cadastro_venda',
            name='tosa_tipo',
            field=models.CharField(choices=[(1, 'Tosa Higiênica'), (2, 'Tosa na Tesoura'), (3, 'Tosa Verão'), (4, 'Tosa na Máquina'), (5, 'Tosa Bebê'), (6, 'Tosa da Raça')], default='1', max_length=50),
        ),
    ]
