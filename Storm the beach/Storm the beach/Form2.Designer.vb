<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Game
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(Game))
        Me.fly_boy = New System.Windows.Forms.Label()
        Me.craftsmans = New System.Windows.Forms.Label()
        Me.gunmans = New System.Windows.Forms.Label()
        Me.days = New System.Windows.Forms.Label()
        Me.Hp_have = New System.Windows.Forms.Label()
        Me.HPs = New System.Windows.Forms.ProgressBar()
        Me.moneys = New System.Windows.Forms.Label()
        Me.bullets_number = New System.Windows.Forms.Label()
        Me.bullets = New System.Windows.Forms.ProgressBar()
        Me.SuspendLayout()
        '
        'fly_boy
        '
        Me.fly_boy.AutoSize = True
        Me.fly_boy.Location = New System.Drawing.Point(899, 121)
        Me.fly_boy.Name = "fly_boy"
        Me.fly_boy.Size = New System.Drawing.Size(89, 18)
        Me.fly_boy.TabIndex = 17
        Me.fly_boy.Text = "0 fly boy"
        Me.fly_boy.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        '
        'craftsmans
        '
        Me.craftsmans.AutoSize = True
        Me.craftsmans.Location = New System.Drawing.Point(899, 89)
        Me.craftsmans.Name = "craftsmans"
        Me.craftsmans.Size = New System.Drawing.Size(107, 18)
        Me.craftsmans.TabIndex = 16
        Me.craftsmans.Text = "0 craftsman"
        '
        'gunmans
        '
        Me.gunmans.AutoSize = True
        Me.gunmans.Location = New System.Drawing.Point(899, 56)
        Me.gunmans.Name = "gunmans"
        Me.gunmans.Size = New System.Drawing.Size(89, 18)
        Me.gunmans.TabIndex = 15
        Me.gunmans.Text = "0 gunman "
        '
        'days
        '
        Me.days.AutoSize = True
        Me.days.Location = New System.Drawing.Point(912, 25)
        Me.days.Name = "days"
        Me.days.Size = New System.Drawing.Size(44, 18)
        Me.days.TabIndex = 14
        Me.days.Text = "Days"
        '
        'Hp_have
        '
        Me.Hp_have.AutoSize = True
        Me.Hp_have.Font = New System.Drawing.Font("SimSun", 14.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(134, Byte))
        Me.Hp_have.Location = New System.Drawing.Point(738, 25)
        Me.Hp_have.Name = "Hp_have"
        Me.Hp_have.Size = New System.Drawing.Size(110, 28)
        Me.Hp_have.TabIndex = 13
        Me.Hp_have.Text = "100/100"
        '
        'HPs
        '
        Me.HPs.Location = New System.Drawing.Point(465, 25)
        Me.HPs.Name = "HPs"
        Me.HPs.Size = New System.Drawing.Size(246, 28)
        Me.HPs.TabIndex = 12
        '
        'moneys
        '
        Me.moneys.AutoSize = True
        Me.moneys.Font = New System.Drawing.Font("SimSun", 14.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(134, Byte))
        Me.moneys.Location = New System.Drawing.Point(324, 25)
        Me.moneys.Name = "moneys"
        Me.moneys.Size = New System.Drawing.Size(26, 28)
        Me.moneys.TabIndex = 11
        Me.moneys.Text = "$"
        '
        'bullets_number
        '
        Me.bullets_number.AutoSize = True
        Me.bullets_number.Font = New System.Drawing.Font("SimSun", 14.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(134, Byte))
        Me.bullets_number.Location = New System.Drawing.Point(260, 24)
        Me.bullets_number.Name = "bullets_number"
        Me.bullets_number.Size = New System.Drawing.Size(26, 28)
        Me.bullets_number.TabIndex = 10
        Me.bullets_number.Text = "7"
        '
        'bullets
        '
        Me.bullets.Location = New System.Drawing.Point(66, 23)
        Me.bullets.Name = "bullets"
        Me.bullets.Size = New System.Drawing.Size(174, 29)
        Me.bullets.TabIndex = 9
        '
        'Game
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(9.0!, 18.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.BackColor = System.Drawing.SystemColors.AppWorkspace
        Me.BackgroundImage = CType(resources.GetObject("$this.BackgroundImage"), System.Drawing.Image)
        Me.ClientSize = New System.Drawing.Size(1924, 1044)
        Me.Controls.Add(Me.fly_boy)
        Me.Controls.Add(Me.craftsmans)
        Me.Controls.Add(Me.gunmans)
        Me.Controls.Add(Me.days)
        Me.Controls.Add(Me.Hp_have)
        Me.Controls.Add(Me.HPs)
        Me.Controls.Add(Me.moneys)
        Me.Controls.Add(Me.bullets_number)
        Me.Controls.Add(Me.bullets)
        Me.Name = "Game"
        Me.Text = "Upgrade "
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents fly_boy As System.Windows.Forms.Label
    Friend WithEvents craftsmans As System.Windows.Forms.Label
    Friend WithEvents gunmans As System.Windows.Forms.Label
    Friend WithEvents days As System.Windows.Forms.Label
    Friend WithEvents Hp_have As System.Windows.Forms.Label
    Friend WithEvents HPs As System.Windows.Forms.ProgressBar
    Friend WithEvents moneys As System.Windows.Forms.Label
    Friend WithEvents bullets_number As System.Windows.Forms.Label
    Friend WithEvents bullets As System.Windows.Forms.ProgressBar
End Class
