Public Class hi

    Public day As Integer = 1
    Public spawn_cooldown_counter As Integer = 40
    Public spawn_cooldown As Integer = 40
    Public money As Integer = 100000
    Public gunman As Integer = 0
    Public craftsman As Integer = 0
    Public fly_boys As Integer = 0
    Public Max_Hp As Integer = 100
    Public Hp As Integer = 100
    Public bullets_have As Integer = 7
    Public bullets_can_have As Integer = 7
    Public damage As Integer = 1
    Public reload_counter As Integer = 15
    Public reload As Integer = 15
    Public spot As Integer = 1

    Private Sub Play_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Play.Click

        Game.Show()

    End Sub

End Class