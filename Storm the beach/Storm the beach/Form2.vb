Public Class Game

    Declare Function GetAsyncKeyState Lib "user32" _
       (ByVal vKey As Long) As Integer

    Dim WithEvents myTimer As New System.Windows.Forms.Timer()

    'Graphics
    Dim Private1 As Image = Image.FromFile("C:\Users\Stone Yao\Desktop\Hi\SD1.png")
    Dim Private2 As Image = Image.FromFile("C:\Users\Stone Yao\Desktop\Hi\SD2.png")
    Dim death_look As Image = Image.FromFile("C:\Users\Stone Yao\Desktop\Hi\death.png")
    Dim defence As Image = Image.FromFile("C:\Users\Stone Yao\Desktop\Hi\defence.png")
    Dim private_attact1 As Image = Image.FromFile("C:\Users\Stone Yao\Desktop\Hi\SD3.png")
    Dim private_attact2 As Image = Image.FromFile("C:\Users\Stone Yao\Desktop\Hi\SD4.png")
    Dim bunker As Image = Image.FromFile("C:\Users\Stone Yao\Desktop\Hi\bunker.png")
    Dim MG42 As Image = Image.FromFile("C:\Users\Stone Yao\Desktop\Hi\Webp.net-resizeimage1.jpg")
    Dim watchtower As Image = Image.FromFile("C:\Users\Stone Yao\Desktop\Hi\Webp.net-resizeimage (142).png")
    Dim Flamethrower As Image = Image.FromFile("C:\Users\Stone Yao\Desktop\Hi\Webp.net-resizeimage2.jpg")
    Dim Artillery As Image = Image.FromFile("C:\Users\Stone Yao\Desktop\Hi\Webp.net-resizeimage231.jpg")
    Dim rocket_artillery As Image = Image.FromFile("C:\Users\Stone Yao\Desktop\Hi\Webp.net-resizeimage12.jpg")
    Dim coastal_artillery As Image = Image.FromFile("C:\Users\Stone Yao\Desktop\Hi\Webp.net-resizeimage342.jpg")
    Dim airport As Image = Image.FromFile("C:\Users\Stone Yao\Desktop\Hi\Webp.net-resizeimagesa.jpg")

    Dim x As Integer = 1
    Dim x1, y1
    Dim EPAOT As Integer = 1 'Number of enemy spawn at one time
    Dim start As Boolean = False
    Dim Mouse_Click As Integer
    Dim day_time As Integer = 200

    'Array
    Dim positionx_array(300) As Integer
    Dim Motion_array(300) As Integer
    Dim positiony_array(300) As Integer
    Dim Enemy_type1_Hp(300) As Integer
    Dim counter_array(300) As Integer
    Dim attack_cooldown_array(300) As Integer

    Private Sub TimerEventProcessor(ByVal myObject As Object, _
       ByVal myEventArgs As EventArgs) _
 Handles myTimer.Tick

        If Mouse_Click = 1 Then

            If hi.bullets_have > 0 And Not start = True Then

                hi.bullets_have = hi.bullets_have - 1
                bullets.Value = hi.bullets_have
                bullets_number.Text = hi.bullets_have

                For i = 1 To EPAOT

                    If x1 > positionx_array(i) - 12 And x1 < positionx_array(i) + 20 And y1 > positiony_array(i) And y1 < positiony_array(i) + 35 And Motion_array(i) >= 1 And Motion_array(i) <= 2 Then

                        Enemy_type1_Hp(i) = Enemy_type1_Hp(i) - hi.damage
                        Exit For

                    ElseIf x1 > positionx_array(i) - 5 And x1 < positionx_array(i) + 25 And y1 > positiony_array(i) And y1 < positiony_array(i) + 35 And Motion_array(i) >= 3 And Motion_array(i) <= 4 Then

                        Enemy_type1_Hp(i) = Enemy_type1_Hp(i) - hi.damage
                        Exit For

                    End If

                Next

            ElseIf Not start = True Then

                hi.bullets_have = 0

            End If

            Mouse_Click = 0

        End If

        If hi.spawn_cooldown_counter < 0 Then 'when the cooldown goes to zero it will spawn enemy

            EPAOT = EPAOT + 1
            hi.spawn_cooldown_counter = hi.spawn_cooldown

        Else

            hi.spawn_cooldown_counter = hi.spawn_cooldown_counter - 1

        End If

        If start = True Then

            hi.reload_counter = hi.reload_counter - 1

            If hi.reload_counter = 0 Then

                hi.reload_counter = hi.reload
                start = False

            End If

        End If

        For i = 1 To EPAOT 'de-spawn the enemy

            If Enemy_type1_Hp(i) = 0 Then

                If counter_array(i) = 30 Then hi.money = hi.money + 50

                counter_array(i) = counter_array(i) - 1

                If counter_array(i) = 0 Then

                    For j = i To EPAOT - 1

                        Motion_array(j) = Motion_array(j + 1)
                        positionx_array(j) = positionx_array(j + 1)
                        Enemy_type1_Hp(j) = Enemy_type1_Hp(j + 1)
                        positiony_array(j) = positiony_array(j + 1)
                        counter_array(j) = counter_array(j + 1)

                    Next

                    Motion_array(EPAOT) = 1
                    positionx_array(EPAOT) = 0
                    Enemy_type1_Hp(EPAOT) = 2
                    positiony_array(EPAOT) = random_int(225, 426)
                    counter_array(EPAOT) = 30

                End If

            End If

        Next

        For i = 0 To EPAOT

            If Motion_array(i) = 4 Then

                If attack_cooldown_array(i) = 3 Then

                    hi.Hp = hi.Hp - 1
                    HPs.Value = hi.Hp
                    Hp_have.Text = hi.Hp & "/" & hi.Max_Hp
                    attack_cooldown_array(i) = attack_cooldown_array(i) - 1

                ElseIf attack_cooldown_array(i) <= 0 Then

                    attack_cooldown_array(i) = 3

                Else

                    attack_cooldown_array(i) = attack_cooldown_array(i) - 1

                End If

            End If

        Next

        day_time = day_time - 1
        If day_time = 0 Then
            shop.Show()
            myTimer.Stop()
        End If

        Me.Invalidate()

    End Sub

    Private Sub Form1_KeyPress(ByVal sender As Object, ByVal e As System.Windows.Forms.KeyPressEventArgs) Handles Me.KeyPress

        If GetAsyncKeyState(82) Then

            hi.bullets_have = hi.bullets_can_have
            bullets.Value = hi.bullets_have
            bullets_number.Text = hi.bullets_have
            start = True

        End If

    End Sub


    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

        Randomize()

        HPs.Minimum = 0
        HPs.Maximum = hi.Max_Hp
        HPs.Value = hi.Hp
        Hp_have.Text = hi.Hp & "/" & hi.Max_Hp

        bullets.Minimum = 0
        bullets.Maximum = hi.bullets_can_have
        bullets.Value = hi.bullets_can_have

        days.Text = "Day " & hi.day
        gunmans.Text = hi.gunman & " gunman"
        craftsmans.Text = hi.craftsman & " craftsman"
        fly_boy.Text = hi.fly_boys & " fly boy"

        myTimer.Interval = 100
        myTimer.Start()

        Me.DoubleBuffered = True

        For i = 1 To 300

            Motion_array(i) = 1

        Next

        For i = 1 To 300

            positiony_array(i) = random_int(225, 426) 'making random spawn location

        Next

        For i = 1 To 300

            Enemy_type1_Hp(i) = 2

        Next

        For i = 1 To 300

            counter_array(i) = 30

        Next

        For i = 1 To 300

            attack_cooldown_array(i) = 3

        Next

    End Sub

    Private Sub Form1_MouseClick(ByVal sender As Object, ByVal e As System.Windows.Forms.MouseEventArgs) Handles Me.MouseClick

        Mouse_Click = 1

    End Sub

    Private Sub Form1_MouseMove(ByVal sender As Object, ByVal e As System.Windows.Forms.MouseEventArgs) Handles Me.MouseMove

        x1 = e.X
        y1 = e.Y

    End Sub

    Private Sub Form1_Paint(ByVal sender As Object, ByVal e As System.Windows.Forms.PaintEventArgs) Handles Me.Paint

        For i = 1 To EPAOT

            If Motion_array(i) = 1 And Not Enemy_type1_Hp(i) = 0 Then

                e.Graphics.DrawImage(Private1, positionx_array(i), positiony_array(i), 20, 35)
                positionx_array(i) = positionx_array(i) + 6
                Motion_array(i) = Motion_array(i) + 1
                If positionx_array(i) >= 520 Then Motion_array(i) = 3

            ElseIf Motion_array(i) = 2 And Not Enemy_type1_Hp(i) = 0 Then

                e.Graphics.DrawImage(Private2, positionx_array(i), positiony_array(i), 20, 35)
                positionx_array(i) = positionx_array(i) + 6
                Motion_array(i) = Motion_array(i) - 1
                If positionx_array(i) >= 520 Then Motion_array(i) = 3

            ElseIf Motion_array(i) = 3 And Not Enemy_type1_Hp(i) = 0 Then

                e.Graphics.DrawImage(private_attact1, positionx_array(i), positiony_array(i), 20, 35)
                Motion_array(i) = Motion_array(i) + 1

            ElseIf Motion_array(i) = 4 And Not Enemy_type1_Hp(i) = 0 Then

                e.Graphics.DrawImage(private_attact2, positionx_array(i) - 6, positiony_array(i), 20, 35)
                Motion_array(i) = Motion_array(i) - 1

            ElseIf Enemy_type1_Hp(i) = 0 Then

                Motion_array(i) = 5
                e.Graphics.DrawImage(death_look, positionx_array(i), positiony_array(i) + 15, 39, 14)

            End If

        Next
        'Dim fontObj As Font = New System.Drawing.Font("Times", 14, FontStyle.Bold)
        'e.Graphics.DrawString(hi.spawn_cooldown_counter, fontObj, Brushes.Black, 200, 200)
        'e.Graphics.DrawString(hi.spawn_cooldown, fontObj, Brushes.Black, 200, 220)

        e.Graphics.DrawImage(defence, 540, 230, 40, 235)
        e.Graphics.DrawImage(bunker, 660, 245, 230, 200)
        moneys.Text = hi.money & "$"

        'e.Graphics.DrawImage(MG42, 660, 195, 67, 52)
        'e.Graphics.DrawImage(MG42, 760, 195, 67, 52)
        'e.Graphics.DrawImage(MG42, 660, 410, 67, 52)
        'e.Graphics.DrawImage(MG42, 760, 410, 67, 52)

        'e.Graphics.DrawImage(MG42, 720, 280, 100, 78)

    End Sub

    Function random_int(ByVal small As Integer, ByVal big As Integer) As Integer

        Return Int(Rnd() * (big - small + 1)) + small

    End Function

End Class