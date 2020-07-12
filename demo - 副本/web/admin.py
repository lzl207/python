from django.contrib import admin
from django.http import JsonResponse
from .models import Powerbase, Powerconsumptionrate

@admin.register(Powerbase)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'Zhibie', 'Leiji', 'Alternator1', 'Main1', 'High1', 'Desulphurization1',
                    'Alternator2', 'Main2', 'High2', 'Desulphurization2', 'Start', 'FactoryA', 'FactoryB', 'add_date','Powerwater')

    # 增加自定义按钮
    actions = ['custom_button']

    def custom_button(self, request, queryset):
        #queryset = Powerbase.objects.all()
        # m = Powerbase.objects.values('Zhibie', 'Leiji', 'Alternator1', 'Main1', 'High1', 'Desulphurization1',
        #             'Alternator2', 'Main2', 'High2', 'Desulphurization2', 'Start', 'FactoryA', 'FactoryB')
        for query in queryset:
            this = query
            m = Powerbase.objects.all().filter(id__lt=this.id).order_by("-id")      # 这里暂时无大碍但是记得改！！！！
            last=m.first()
            n = Powerbase.objects.filter(id=this.id)[0]

            Powergeneration1 = (this.Alternator1 - last.Alternator1) * 100  # AO
            Powermain1 = (this.Main1 - last.Main1) * 550  # AP
            Powerhigh1 = (this.High1 - last.High1) * 10  # AQ
            Powerdesulphurization1 = (this.Desulphurization1 - last.Desulphurization1) * 5  # AR
            Powergeneration2 = (this.Alternator2 - last.Alternator2) * 100  # AS
            Powermain2 = (this.Main2 - last.Main2) * 550  # AT
            Powerhigh2 = (this.High2 - last.High2) * 10  # AU
            Powerdesulphurization2 = (this.Desulphurization2 - last.Desulphurization2) * 5  # AV
            Standbysubstation = (this.Start - last.Start) * 66  # BA  启备变电量,
            Powergeneration_all = Powergeneration1 + Powergeneration2 # BD  总发电量,
            PowerFactoryA = (this.FactoryA - last.FactoryA) * 0.24  # BL  A厂前区变电量,
            PowerFactoryB = (this.FactoryB - last.FactoryB) * 0.24  # BM  B厂前区变电量,
            PowerFactory_all = PowerFactoryA + PowerFactoryB  # BN  厂前区变电量,
            Powerdesulphurization_all = Powerdesulphurization1 + Powerdesulphurization2  # BF 总脱硫耗电量,
            Ongridenergy1 = Powermain1 - Standbysubstation * Powergeneration1 / Powerdesulphurization_all  # AW  1机上网电量,
            PowerMachineryFactory1 = Powerhigh1 + Powerdesulphurization1 - PowerFactory_all * Powergeneration1 / Powergeneration_all  # AX 1机厂用电量,
            Ongridenergy2 = Powermain2 - Standbysubstation * Powergeneration2 / Powerdesulphurization_all      # AY 2机上网电量,
            PowerMachineryFactory2 = Powerhigh2 + Powerdesulphurization2 - PowerFactory_all * Powergeneration2 / Powergeneration_all  # AZ 2机厂用电量,                                             #
            Ongridenergy_all = Ongridenergy1 + Ongridenergy2  # BB 总上网电量,
            PowerMachineryFactory_all = PowerMachineryFactory1 + PowerMachineryFactory2  # BC总厂用电量,
            Powermain_all = Powermain1 + Powermain2  # BD 总主变电量,
            Desulfurizationdesulphurization1 = Powerdesulphurization1 / Powergeneration1 * 100  # BG 1机脱硫电耗,
            Desulfurizationdesulphurization2 = Powerdesulphurization2 / Powergeneration2 * 100  # BI 2机脱硫电耗
            Desulfurizationdesulphurization_all = (Powerdesulphurization1 + Powerdesulphurization2) / Powergeneration_all * 100  # BK 总脱硫电耗,

            Poweruse1 = PowerMachineryFactory1 / Powergeneration1 * 100  # AD 1机厂用电率,
            Poweruse2 = PowerMachineryFactory2 / Powergeneration2 * 100  # AE 2机厂用电率,
            Poweruse_all = (PowerMachineryFactory1 + PowerMachineryFactory2) / Powermain_all * 100  # AF 全厂用电率,
            Comprehensive1 = (Powergeneration1 - Ongridenergy1) / Powergeneration1 * 100  # AG 1机综合厂用电率,
            Comprehensive2 = (Powergeneration2 - Ongridenergy2) / Powergeneration2 * 100  # AH 2机综合厂用电率,
            Comprehensive_all = (Powergeneration_all - Ongridenergy_all) / Powergeneration_all * 100  # AI 全厂综合厂用电率,

            LM = 24
            if this.Leiji == "xiaye":
                LM = 5
            elif this.Leiji == "shangye":
                LM = 6
            elif this.Leiji == "zaoban" or this.Leiji == "zhongban":
                LM = 6.5
            Load1 = Powergeneration1 / 60 / LM * 100  # AJ 1机发电负荷率,
            Load2 = Powergeneration2 / 60 / LM * 100  # AK 2机发电负荷率,
            Load_all = (Powergeneration1 * Load1 + Powergeneration2 * Load2) / Powermain_all  # AL 全场发电负荷率,

            filter_dic = dict()
            filter_dic["Powergeneration1"] =round(Powergeneration1)
            filter_dic["Powermain1"] =round(Powermain1,3)
            filter_dic["Powerhigh1"] =round(Powerhigh1,2)
            filter_dic["Powerdesulphurization1"] =round(Powerdesulphurization1,2)
            filter_dic["Powergeneration2"] =round(Powergeneration2,2)
            filter_dic["Powermain2"] =round(Powermain2,3)
            filter_dic["Powerhigh2"] =round(Powerhigh2,2)
            filter_dic["Powerdesulphurization2"] =round(Powerdesulphurization2,2)
            filter_dic["Standbysubstation"] =round(Standbysubstation,3)
            filter_dic["Powergeneration_all"] =round(Powergeneration_all)
            filter_dic["PowerFactoryA"] =round(PowerFactoryA,2)
            filter_dic["PowerFactoryB"] =round(PowerFactoryB,2)
            filter_dic["PowerFactory_all"] =round(PowerFactory_all,2)
            filter_dic["Powerdesulphurization_all"] =round(Powerdesulphurization_all,2)
            filter_dic["Ongridenergy1"] =round(Ongridenergy1,4)
            filter_dic["PowerMachineryFactory1"] =round(PowerMachineryFactory1,4)
            filter_dic["Ongridenergy2"] =round(Ongridenergy2,4)
            filter_dic["PowerMachineryFactory2"] =round(PowerMachineryFactory2,4)
            filter_dic["Ongridenergy_all"] =round(Ongridenergy_all,4)
            filter_dic["PowerMachineryFactory_all"] =round(PowerMachineryFactory_all,4)
            filter_dic["Powermain_all"] =round(Powermain_all)
            filter_dic["Desulfurizationdesulphurization1"] =round(Desulfurizationdesulphurization1,2)
            filter_dic["Desulfurizationdesulphurization2"] =round(Desulfurizationdesulphurization2,2)
            filter_dic["Desulfurizationdesulphurization_all"] =round(Desulfurizationdesulphurization_all,2)
            filter_dic["Poweruse1"] =round(Poweruse1,2)
            filter_dic["Poweruse2"] =round(Poweruse2,2)
            filter_dic["Poweruse_all"] =round(Poweruse_all,2)
            filter_dic["Comprehensive1"] =round(Comprehensive1,2)
            filter_dic["Comprehensive2"] =round(Comprehensive2,2)
            filter_dic["Comprehensive_all"] =round(Comprehensive_all,2)
            filter_dic["Load1"] =round(Load1,2)
            filter_dic["Load2"] =round(Load2,2)
            filter_dic["Load_all"] =round(Load_all,2)

            caculate=Powerconsumptionrate.objects.filter(baseid=this.id)
            if caculate:
                caculate.update(**filter_dic)
            else:
                filter_dic["baseid"]=n
                Powerconsumptionrate.objects.create(**filter_dic)



     #   return JsonResponse("true", safe=False)


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



