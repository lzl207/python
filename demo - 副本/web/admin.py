from django.contrib import admin
from .models import Powerbase, Powerconsumptionrate

@admin.register(Powerbase)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'Zhibie', 'Leiji', 'Alternator1', 'Main1', 'High1', 'Desulphurization1',
                    'Alternator2', 'Main2', 'High2', 'Desulphurization2', 'Start', 'FactoryA', 'FactoryB', 'add_date')

    # 增加自定义按钮
    actions = ['custom_button']

    def custom_button(self, request, queryset):
        queryset = Powerbase.objects.all()
        # m = Powerbase.objects.values('Zhibie', 'Leiji', 'Alternator1', 'Main1', 'High1', 'Desulphurization1',
        #             'Alternator2', 'Main2', 'High2', 'Desulphurization2', 'Start', 'FactoryA', 'FactoryB')
        m = Powerbase.objects.all()
        print(m)
        # c = []
        # for i in m:
        #     for key, value in i.items():
        #         c.append(value)
        # print(c)
    # 用电率(黄色表格)
    # Poweruse1:#1机厂用电率,  Poweruse2:#2机厂用电率,  Poweruse_all:全厂用电率,  Comprehensive1:#1机综合厂用电率,  Comprehensive2:#2机综合厂用电率,
    # Comprehensive_all:全厂综合厂用电率,  Load1:#1机发电负荷率,  Load2:#2机发电负荷率,  Load_all:全场发电负荷率,
    # 用电量(蓝色表格)
    # Powergeneration1:#1机发电量,  Powermain1:#1机主变电量,  Powerhigh1:#1高厂变电量,  Powerdesulphurization1:#1机脱硫电量,
    # Powergeneration2:#2机发电量,  Powermain2:#2机主变电量,  Powerhigh2:#2高厂变电量,  Powerdesulphurization2:#2机脱硫电量,
    # Ongridenergy1:#1机上网电量,  PowerMachineryFactory1:#1机厂用电量,   Ongridenergy2:#2机上网电量,  PowerMachineryFactory2:#2机厂用电量,
    # Standbysubstation:#启备变电量,  Ongridenergy_all:#总上网电量,  PowerMachineryFactory_all:总厂用电量,  Powergeneration_all:总发电量,  Powermain_all:总主变电量,
    # Powerdesulphurization_all:总脱硫耗电量,  Desulfurizationdesulphurization1:#1机脱硫电耗,  Desulfurizationdesulphurization2:#2机脱硫电耗
    # Desulfurizationdesulphurization_all:总脱硫电耗,  PowerFactoryA:A厂前区变电量,  PowerFactoryB:B厂前区变电量,  PowerFactory_all:厂前区变电量,  Powerwater:全厂制水电耗
    auto = Powerconsumptionrate()









    # 显示的文本，与django admin一致
    custom_button.short_description = '自动计算'
    # icon，参考element-ui icon与https://fontawesome.com
    custom_button.icon = 'fas fa-audio-description'

    # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    custom_button.type = 'danger'

    # 给按钮追加自定义的颜色
    custom_button.style = 'color:black;'



