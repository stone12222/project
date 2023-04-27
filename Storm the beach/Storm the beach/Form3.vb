Public Class shop

    Dim bullets_have As Integer
    Dim damage As Integer
    Dim reload As Integer
    Dim cost As Integer
    Dim type As Integer 'type 1 is tower and type 2 is gun
    Dim gun As Integer

    Private Sub watchtower_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles tower1.Click

        about.Text = "A watchtower is a type of fortification used in many parts of the world. It differs from a regular tower in that its primary use is military and from a turret in that it is usually a freestanding structure. Its main purpose is to provide a high, safe place from which a sentinel or guard may observe the surrounding area. In some cases, non-military towers, such as religious towers, may also be used as watchtowers. Cost: $2000"
        cost = 2000
        type = 1

    End Sub

    Private Sub mg42_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles tower2.Click

        about.Text = "The MG 42 (shortened from German: Maschinengewehr 42, or machine gun 42) is a 7.92×57mm Mauser general-purpose machine gun designed in Nazi Germany and used extensively by the Wehrmacht and the Waffen-SS during the second half of World War II. It was intended to replace the earlier MG 34, which was more expensive and took much longer to produce, but both weapons were produced until the end of World War II. Cost: $2000"
        cost = 2000
        type = 1

    End Sub

    Private Sub Flamethrower_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles tower3.Click

        about.Text = "A flamethrower is a mechanical incendiary device designed to project a long, controllable stream of fire. First deployed by the Greeks in the 1st century CE, flamethrowers saw use in modern times during World War I, and more widely in World War II. Cost: $4000"
        cost = 4000
        type = 1

    End Sub

    Private Sub Artillery_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles tower4.Click

        about.Text = "Artillery is a class of heavy military ranged weapons built to launch munitions far beyond the range and power of infantry's small arms. Early artillery development focused on the ability to breach defensive walls and fortifications during sieges, and led to heavy, fairly immobile siege engines. As technology improved, lighter, more mobile field artillery cannons developed for battlefield use. This development continues today; modern self-propelled artillery vehicles are highly mobile weapons of great versatility providing the large share of an army's total firepower. Cost: $6000"
        cost = 6000
        type = 1

    End Sub

    Private Sub rocket_artillery_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles tower5.Click

        about.Text = "Rocket artillery is a type of artillery which utilizes rockets as a projectile, the use of rocket artillery dates back to medieval China where devices such as fire arrows were used (albeit mostly as a psychological weapon). Fire arrows were also used in multiple launch systems and transported via carts. By the late nineteenth century, due to improvements in the power and range of conventional artillery, the use of early military rockets declined; they were finally used on a small scale by both sides during the American Civil War. Cost: $ 8000"
        cost = 8000
        type = 1

    End Sub

    Private Sub coastal_artillery_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles tower6.Click

        about.Text = "Coastal artillery is the branch of the armed forces concerned with operating anti-ship artillery or fixed gun batteries in coastal fortifications. Cost: $9000"
        cost = 9000
        type = 1

    End Sub

    Private Sub airport_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles tower7.Click

        about.Text = "An airport solely serving helicopters is called a heliport. An airport for use by seaplanes and amphibious aircraft is called a seaplane base. Such a base typically includes a stretch of open water for takeoffs and landings, and seaplane docks for tying-up. Hartsfield–Jackson Atlanta International Airport in USA is the busiest and biggest airport in the world. Cost: $10000"
        cost = 10000
        type = 1

    End Sub

    Private Sub shop_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

        money.Text = "money: " & hi.money

    End Sub

    Private Sub Label13_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Label13.Click

        gun1.Visible = True
        gun1.Enabled = True
        gun2.Visible = True
        gun2.Enabled = True
        gun3.Visible = True
        gun3.Enabled = True
        gun4.Visible = True
        gun4.Enabled = True
        gun5.Visible = True
        gun5.Enabled = True
        gun6.Visible = True
        gun6.Enabled = True
        gun7.Visible = True
        gun7.Enabled = True
        gun8.Visible = True
        gun8.Enabled = True

        tower1.Visible = False
        tower1.Enabled = False
        tower2.Visible = False
        tower2.Enabled = False
        tower3.Visible = False
        tower3.Enabled = False
        tower4.Visible = False
        tower4.Enabled = False
        tower5.Visible = False
        tower5.Enabled = False
        tower6.Visible = False
        tower6.Enabled = False
        tower7.Visible = False
        tower7.Enabled = False
        tower8.Visible = False
        tower8.Enabled = False

    End Sub

    Private Sub Label12_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Label12.Click

        gun1.Visible = False
        gun1.Enabled = False
        gun2.Visible = False
        gun2.Enabled = False
        gun3.Visible = False
        gun3.Enabled = False
        gun4.Visible = False
        gun4.Enabled = False
        gun5.Visible = False
        gun5.Enabled = False
        gun6.Visible = False
        gun6.Enabled = False
        gun7.Visible = False
        gun7.Enabled = False
        gun8.Visible = False
        gun8.Enabled = False

        tower1.Visible = True
        tower1.Enabled = True
        tower2.Visible = True
        tower2.Enabled = True
        tower3.Visible = True
        tower3.Enabled = True
        tower4.Visible = True
        tower4.Enabled = True
        tower5.Visible = True
        tower5.Enabled = True
        tower6.Visible = True
        tower6.Enabled = True
        tower7.Visible = True
        tower7.Enabled = True
        tower8.Visible = True
        tower8.Enabled = True

    End Sub

    Private Sub gun1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles gun1.Click

        about.Text = "Luger Ammo: 10 Damage: 1 Reload: 1.5 Cost: 500"
        bullets_have = 10
        damage = 1
        reload = 1.5
        cost = 500
        type = 2
        gun = 1

    End Sub

    Private Sub gun2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles gun2.Click

        about.Text = "98k Ammo: 5 Damage: 4 Reload: 1.5 Cost: 1000"
        bullets_have = 5
        damage = 4
        reload = 15
        cost = 1000
        type = 2
        gun = 2

    End Sub

    Private Sub gun3_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles gun3.Click

        about.Text = "G43 Ammo: 15 Damage: 4 Reload: 1 Cost: 2000"
        bullets_have = 15
        damage = 3
        reload = 10
        cost = 2000
        type = 2
        gun = 3

    End Sub

    Private Sub gun4_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles gun4.Click

        about.Text = "MP34 Ammo: 25 Damage: 1 Reload: 1.5 Cost: 2500"
        bullets_have = 25
        damage = 1
        reload = 10
        cost = 2500
        type = 2
        gun = 4

    End Sub

    Private Sub gun5_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles gun5.Click

        about.Text = "MP18 Ammo: 60 Damage: 1 Reload: 3 Cost: 3000"
        bullets_have = 60
        damage = 1
        reload = 30
        cost = 3000
        type = 2
        gun = 5

    End Sub


    Private Sub gun6_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles gun6.Click

        about.Text = "MP40 Ammo: 35 Damage: 2 Reload: 1 Cost: 4000"
        bullets_have = 35
        damage = 2
        reload = 10
        cost = 4000
        type = 2
        gun = 6

    End Sub

    Private Sub gun7_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles gun7.Click

        about.Text = "STG44 Ammo: 40 Damage: 3 Reload: 0.5 Cost: 5000"
        bullets_have = 25
        damage = 3
        reload = 5
        cost = 5000
        type = 2
        gun = 7

    End Sub

    Private Sub gun8_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles gun8.Click

        about.Text = "MG42 Ammo: 500 Damage: 1 Reload: 3 Cost: 6500"
        bullets_have = 500
        damage = 1
        reload = 30
        cost = 6500
        type = 2
        gun = 8

    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Buy.Click

        If hi.money >= cost Then
            Select Case type
                Case 1
                Case 2

                    hi.bullets_have = bullets_have
                    hi.bullets_can_have = bullets_have
                    hi.damage = damage
                    hi.reload_counter = reload
                    hi.reload = reload
                    hi.money = hi.money - cost
                    money.Text = "money: " & hi.money

            End Select
        End If

    End Sub

    Private Sub next_day_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles next_day.Click

        hi.day = hi.day + 1
        Game.Close()
        Game.Show()
        Me.Close()

    End Sub

    Private Sub PictureBox1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Gunman.Click

        If hi.money >= 200 Then

            hi.gunman = hi.gunman + 1
            hi.money = hi.money - 200
            money.Text = "money: " & hi.money

        End If

    End Sub

    Private Sub Craftsman_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Craftsman.Click

        If hi.money >= 400 Then

            hi.craftsman = hi.craftsman + 1
            hi.money = hi.money - 400
            money.Text = "money: " & hi.money

        End If

    End Sub

    Private Sub Fly_boy_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Fly_boy.Click

        If hi.money >= 1000 Then

            hi.fly_boys = hi.fly_boys + 1
            hi.money = hi.money - 1000
            money.Text = "money: " & hi.money

        End If

    End Sub

    Private Sub upgarde_wall_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles upgarde_wall.Click

        If hi.money >= 800 Then

            hi.money = hi.money - 800
            money.Text = "money: " & hi.money
            hi.Max_Hp = hi.Max_Hp + 20
            hi.Hp = hi.Hp + 20

        End If

    End Sub

    Private Sub repair_bunker_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles repair_bunker.Click

        If hi.money >= 100 Then

            hi.money = hi.money - 100
            money.Text = "money: " & hi.money
            hi.Hp = hi.Hp + 20
            If hi.Hp > hi.max_hp Then hi.Hp = 100

        End If

    End Sub
End Class